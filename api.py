# Import flask and datetime module for showing date and time
from flask import Flask, request, jsonify
from imageProcessing import DataUpload, compare_with_database, video_imgSplit, modelLoad
import json
import os
from flask_cors import CORS


UPLOAD_FOLDER = 'LocalFiles'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'MOV'}  # Adjust based on your needs

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app)


@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Save or process your file here. You could do:
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    content_type = request.form.get('content_type')
    uploadID = request.form.get('uploadID')
    
    # Call your method, but adjust it to use the saved file_path.
    uploaded_data = video_imgSplit(file_path, content_type, uploadID)
    DataUpload(uploaded_data)

    return jsonify({'message': 'Data uploaded successfully'})

@app.route('/compare', methods=['POST'])
def compare():
    data = request.json
    
    img_paths = data.get('img_paths')
    matched_records = compare_with_database(img_paths, modelLoad())
    
    # Return matched records as JSON, you may need to serialize the records appropriately
    return jsonify({'matches': matched_records})

 
     
# Running app
if __name__ == '__main__':
    app.run(debug=True)