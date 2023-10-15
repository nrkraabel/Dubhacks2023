# Import flask and datetime module for showing date and time
from flask import Flask, request, jsonify
from imageProcessing import DataUpload, compare_with_database, video_imgSplit, modelLoad
import json
import os
import requests
from flask_cors import CORS
from werkzeug.utils import secure_filename
import shutil
import uuid



UPLOAD_FOLDER = 'LocalFiles'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'MOV'}  # Adjust based on your needs
app = Flask(__name__)

#@app.route('/shareForm', methods=['POST'])
#def createShare():
    #sform = ShareForm()
    #if validate
        #new upload
        #


# Running app
if __name__ == '__main__':
    app.run(debug=True)