from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 1. Define the structure of our incoming microgrid sensor data
class SensorData(BaseModel):
    sensor_id: str
    frequency_deviation: float
    tie_line_power: float

# 2. Our original status check endpoint
@app.get("/")
def read_root():
    return {"status": "Microgrid Security API is running!"}

# 3. Our new endpoint to receive data and check for FDI attacks
@app.post("/detect-fdi")
def analyze_sensor_data(data: SensorData):
    # Basic logic: If the frequency deviation is unnaturally high, flag it
    is_attack = False
    if data.frequency_deviation > 0.05 or data.frequency_deviation < -0.05:
        is_attack = True
        
    return {
        "sensor_analyzed": data.sensor_id,
        "fdi_detected": is_attack,
        "received_deviation": data.frequency_deviation
    }