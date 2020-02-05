import unittest
import flask
from api import app

class TestAPI(unittest.TestCase):
    
    def test_init_API(self):
        print("test")
        #result = app.run(debug=True)
 
        self.assertIsInstance(app, flask.app.Flask, "Should be equal and works")
        
if __name__ == "__main__":
    unittest.main()