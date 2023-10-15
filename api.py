# Import flask and datetime module for showing date and time
from flask import Flask
from flask_cors import CORS
from faceMatchDriver import modelLoad, get_embedding, image_difference_detection 
app = Flask(__name__)
CORS(app)

 
# Route for seeing a data
@app.route('/data', methods=['POST'])
def data_route():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return jsonify({"error": "No file part"}), 400
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400
        if file:
            filename = f"received_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.png"
            file_path = os.path.join(".", filename)
            file.save(file_path)
            return jsonify({"message": f"File saved as {filename}"}), 200
    return jsonify({"message": "Use POST to send data"})

 
     
# Running app
if __name__ == '__main__':
    app.run(debug=True)