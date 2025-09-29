from flask import Flask, request, send_file
from flask_cors import CORS
import os
import tempfile
import zipfile

app = Flask(__name__)
CORS(app, origins=["*"])

@app.route('/cryp', methods=['POST'])
def encrypt_files() :
    if 'files' not in request.files :
        return "No files uploaded", 400
    
    files = request.files.getlist('files')

    for file in files : 
        print(f"received : {file.filename}", flush=True)
        #Do encryption and return
        #>Create an empty encrypted_files
        #>Add the newly encrypted file in to the new array

    tmp_fd, tmp_path = tempfile.mkstemp(suffix=".zip")
    os.close(tmp_fd)

    with zipfile.ZipFile(tmp_path, 'w') as zf :
        for file in files : #When encryption done, replace this array
            file.seek(0)
            zf.writestr(file.filename, file.read())

    return send_file(tmp_path, as_attachment=True, download_name="files")

if __name__ == "__main__" :
    app.run(port=5000, debug=True)