from flask import Flask, request, send_file
from flask_cors import CORS
import os

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

    return "Succes", 200

if __name__ == "__main__" :
    app.run(port=5000, debug=True)