import unittest
from imageProcessing import *
from SQLAccess import *

class TestFunctions(unittest.TestCase):

    def test_detect_faces(self):
        img_path = '0000005.jpg'
        img = cv2.imread(img_path)
        result = detect_faces(img, 1)
        self.assertIsNotNone(result)  

    def test_DataUpload(self):
        data = [["1", 1, "embedding_str", 0, 0, 0]]
        DataUpload(data)


    def test_video_imgSplit(self):
        video_path = 'vid.mov'
        result = video_imgSplit(video_path, 'video', 1)
        self.assertIsNotNone(result)

    def test_modelLoad(self):
        model = modelLoad()
        self.assertIsNotNone(model)
        
    def test_get_embedding(self):
        model = modelLoad()
        img_path = '0014_0002593_script.jpg'
        embedding = get_embedding(img_path, model)
        self.assertIsNotNone(embedding)

    def test_similarity(self):
        embedding1 = torch.tensor([1.0, 0.0])
        embedding2 = torch.tensor([0.0, 1.0])
        result = similarity(embedding1, embedding2)
        self.assertEqual(result, 0.0)  # Orthogonal vectors, similarity should be 0

    def test_pull_data(self):
        result = pull_data(100)
        self.assertTrue(isinstance(result, list))

    def test_compare_with_database(self):
        model = modelLoad()
        img_paths = ['Beauty.jpg', 'Beauty2.jpg']
        results = compare_with_database(img_paths, model)
        self.assertTrue(isinstance(results, list))
        self.assertEqual(len(results), len(img_paths))

    def test_extract_lat_long(self):
        img_path = 'geoTaggedTest.jpg'  # Make sure this image contains GPS metadata for this test
        lat, lon = extract_lat_long(img_path)
        # Assuming you know the latitude and longitude values for the test image:
        expected_lat = 47.55287591428486   # Replace with the correct value
        expected_lon = -122.31833228133286  # Replace with the correct value
        self.assertAlmostEqual(lat, expected_lat, places=3)
        self.assertAlmostEqual(lon, expected_lon, places=3)

    def test_predict_Geo(self):

        # Use a test image for geo location prediction
        img_path = 'geoTaggedTest.jpg' 

        lat, lon = predict_Geo(img_path)

        expected_lat = 33
        
        expected_lon = 47


        self.assertIsNotNone(lat, "Latitude prediction should not be None")
        self.assertIsNotNone(lon, "Longitude prediction should not be None")
        self.assertAlmostEqual(lat, expected_lat, places=0)
        self.assertAlmostEqual(lon, expected_lon, places=0)

    def clear_datatests(self):
        ds = SQLAccess()
        ds.clear_dataset()
        result = pull_data(100)
        self.assertEqual(len(result), 0)

        

if __name__ == '__main__':
    unittest.main()
