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
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app, origins="http://localhost:3000", supports_credentials=True)


@app.route('/upload', methods=['POST'])
def upload():
    urls = request.json.get('urls')
    if not urls or not isinstance(urls, list):
        return jsonify({'error': 'No URLs provided or URLs are not in a list format'}), 400

    results = []
    for url in urls:
        # Download the file from Google Drive
        response = request.get(url, allow_redirects=True)
        if response.status_code != 200:
            results.append({'url': url, 'status': 'failed', 'reason': 'Unable to download'})
            continue

        file_path = os.path.join(UPLOAD_FOLDER, "tempfile")  # Generate unique filenames based on your needs
        with open(file_path, 'wb') as f:
            f.write(response.content)
        content_type = 'picture' 
        
        if content_type == 'picture':
            video_imgSplit(file_path, "picture", 0)  # Assuming you've defined video_imgSplit elsewhere
        else:
            # Handle videos, assuming video_imgSplit can handle videos too
            video_imgSplit(file_path, "video", 0)

        # Process the file (place your file processing code here)
        # Example: uploaded_data = process_file(file_path)
        uploaded_data = "worked"

        results.append({'url': url, 'status': 'success', 'data': uploaded_data})

    return jsonify(results)

@app.route('/compare', methods=['POST'])
def compare():
    print(request)
    # Check if the request contains files
    if 'image0' not in request.files:
        return jsonify({'error': 'No image files provided'}), 400

    temp_img_paths = []

    # Iterating through all the uploaded files
    index = 0
    while f'image{index}' in request.files:
        file = request.files[f'image{index}']

        # Check if the file is not empty
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        if file and file.filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS:
            filename = secure_filename(file.filename)
            temp_filename = os.path.join("temporary_directory", filename)
            file.save(temp_filename)
            temp_img_paths.append(temp_filename)
        
        index += 1

    matched_records = compare_with_database(temp_img_paths, modelLoad())

    # Clean up the temporarily stored images
    for path in temp_img_paths:
        os.remove(path)

    # Return matched records as JSON
    return jsonify({'matches': matched_records})

 
     
# Running app
if __name__ == '__main__':
    app.run(debug=True)