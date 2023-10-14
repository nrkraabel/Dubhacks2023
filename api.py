# Import flask and datetime module for showing date and time
from flask import Flask
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
import datetime
 
x = str(datetime.datetime.now())
 

 
# Route for seeing a data
@app.route('/data', methods=['GET', 'POST'])
def get_time():
 
    # Returning an api for showing in  reactjs
    return {
        'Name':"Nick", 
        "Age":"22",
        "Date":x, 
        "programming":"python"
        }
 
     
# Running app
if __name__ == '__main__':
    app.run(debug=True)