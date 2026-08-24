import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# 1. Boundary Value Analysis (Testing the absolute edges of the threshold)
@pytest.mark.parametrize("deviation, expected_result", [
    (0.00, False),     # Normal nominal operation
    (0.05, False),     # Exact positive boundary limit
    (0.051, True),     # Just outside positive boundary (Attack detected)
    (-0.05, False),    # Exact negative boundary limit
    (-0.051, True),    # Just outside negative boundary (Attack detected)
    (5.00, True),      # Extreme numerical spike
])
def test_fdi_boundaries(deviation, expected_result):
    # This automatically runs 6 separate times using the data list above
    response = client.post("/detect-fdi", json={
        "sensor_id": "Grid_Node_BVA",
        "frequency_deviation": deviation,
        "tie_line_power": 10.0
    })
    assert response.status_code == 200
    assert response.json()["fdi_detected"] == expected_result

# 2. Negative Testing (Testing how the system handles invalid data formats)
def test_invalid_data_type():
    # Sending a text string instead of a decimal number for tie_line_power
    response = client.post("/detect-fdi", json={
        "sensor_id": "Grid_Node_Error",
        "frequency_deviation": 0.01,
        "tie_line_power": "System_Fault" 
    })
    
    # 422 is the standard web code for "Unprocessable Entity" (Data rejected)
    # This proves the API correctly defends itself against bad data
    assert response.status_code == 422