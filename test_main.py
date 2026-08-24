from fastapi.testclient import TestClient
from main import app

# Create a virtual client to send signals to our API
client = TestClient(app)

def test_normal_operation():
    # 1. Send normal grid data
    response = client.post("/detect-fdi", json={
        "sensor_id": "Grid_Node_02",
        "frequency_deviation": 0.01,
        "tie_line_power": 10.0
    })
    
    # 2. Check if the API accepted the data (Status Code 200 means OK)
    assert response.status_code == 200
    
    # 3. Check if the logic correctly flagged it as NOT an attack
    assert response.json()["fdi_detected"] == False

def test_attack_detection():
    # 1. Send manipulated data (frequency deviation is outside the 0.05 threshold)
    response = client.post("/detect-fdi", json={
        "sensor_id": "Grid_Node_03",
        "frequency_deviation": 0.09,
        "tie_line_power": 10.0
    })
    
    # 2. Verify it was accepted
    assert response.status_code == 200
    
    # 3. Verify the logic correctly flagged it AS an attack
    assert response.json()["fdi_detected"] == True