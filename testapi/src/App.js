import React, { useState } from 'react';
import './App.css';

function App() {

  const [selectedFile, setSelectedFile] = useState(null);
  const [imgPaths, setImgPaths] = useState([]);
  const [matches, setMatches] = useState(null);

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };
  const handleUpload = async () => {
    try {
        const formData = new FormData();
        formData.append('file', selectedFile);
        const content_type = "picture";  // or "video"
        formData.append('content_type', content_type);
        const uploadID = "some_upload_id";  // Replace with actual upload ID
        formData.append('uploadID', uploadID);

        const response = await fetch("http://localhost:5000/upload", {
            method: "POST",
            body: formData
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
          
          const data = await response.json();
          console.log(data);
      } catch (error) {
        console.error("There was an error uploading the file:", error);
    }
};


  const handleCompare = async () => {
    try {
      const response = await fetch("http://localhost:5000/compare", {
        method: "POST",
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          img_paths: imgPaths
        })
      });
  
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
  
      const data = await response.json();
      setMatches(JSON.stringify(data.matches));
    } catch (error) {
      console.log("There was a problem with the fetch operation:", error.message);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <input type="file" onChange={handleFileChange} />
        <button onClick={handleUpload}>Upload Data</button>

        <div>
          <input type="text" onChange={e => setImgPaths([...imgPaths, e.target.value])} placeholder="Add Image Path" />
          <button onClick={handleCompare}>Compare Images</button>
          {matches && <div>
            Matched Records: {matches}
          </div>}
        </div>
      </header>
    </div>
  );
}

export default App;
