from flask import app, send_file
from download import filename
from sheetProcess import process_data, process_file
import os                                                                                   

@app.route('/download')

def download_file():
    filename = process_file()
    
    return send_file(os.path.join('uploads', filename), as_attachment=True)
