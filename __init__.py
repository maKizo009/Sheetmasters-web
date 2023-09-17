import json
from flask import Flask, app, render_template, jsonify
import upload
import download
import sheetProcess

app = Flask(__name__)

processing_completed = False

if __name__ == "__main__":
    app.run(port=8000)

@app.route('/')

def home():
  
    return render_template('index.html', upload)


@app.route('/status')

def status():
    if sheetProcess.process_file:

         return jsonify({
             'status': 'completed' 
             if  processing_completed
             else 'processing'})
             
    return download


    



