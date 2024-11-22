import pytest
from fastapi.testclient import TestClient
from app.app import app  # Assuming your FastAPI app is in 'app.py'

# Initialize the test client
client = TestClient(app)

# Test the home route (GET /)
# def test_home():
#     response = client.get("/")
#     assert response.status_code == 200
#     assert "home.html" in response.text  # Make sure the correct template is loaded

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    # Check for specific content in the HTML
    assert "<title>Iris Classification Prediction</title>" in response.text  # Example: Check the title tag
    assert "<form" in response.text  # Example: Check for a form tag in the rendered HTML


# Test the /predict route with form data (POST /predict)
def test_predict():
    # Example data to send in the form
    form_data = {
        "SepalLengthCm": 5.1,
        "SepalWidthCm": 3.5,
        "PetalLengthCm": 1.4,
        "PetalWidthCm": 0.2
    }
    
    # Sending POST request with form data
    response = client.post("/predict", data=form_data)
    
    # Assert the status code is 200
    assert response.status_code == 200
    
    # Check if the prediction result is displayed in the response
    assert "The Flower prediction is" in response.text

# Test invalid data (e.g., missing a required field in the form)
def test_predict_invalid_data():
    form_data = {
        "SepalLengthCm": 5.1,
        "SepalWidthCm": 3.5,
        "PetalLengthCm": 1.4
        # Missing PetalWidthCm
    }
    
    response = client.post("/predict", data=form_data)
    
    # Assert the status code is 422 (Unprocessable Entity) due to missing field
    assert response.status_code == 422

# Test prediction edge case (e.g., input values at extremes)
def test_predict_edge_case():
    form_data = {
        "SepalLengthCm": 0.1,  # Minimal value
        "SepalWidthCm": 10.0,  # Arbitrarily large value
        "PetalLengthCm": 0.1,  # Minimal value
        "PetalWidthCm": 10.0   # Arbitrarily large value
    }
    
    response = client.post("/predict", data=form_data)
    assert response.status_code == 200
    assert "The Flower prediction is" in response.text

