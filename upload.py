from crypt import methods
from fileinput import filename
from flask import Flask, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

@app.route("/upload", methods=['POST'])

def upload_file():

    if 'file' in request.files:
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join('uploads'), filename)

        return filename