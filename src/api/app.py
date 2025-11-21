from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

# ---------- 1. Feature list (must match training exactly) ----------
FEATURES = [
    "machine_id",
    "temperature",
    "vibration",
    "pressure",
    "current",
    "rpm",
    "status_code",
    "temp_mean_6h",
    "temp_std_6h",
    "vib_mean_6h",
    "vib_std_6h",
    "temp_mean_12h",
    "temp_std_12h",
    "vib_mean_12h",
    "vib_std_12h",
    "temp_mean_24h",
    "temp_std_24h",
    "vib_mean_24h",
    "vib_std_24h",
    "temp_delta_1h",
    "vib_delta_1h",
    "temp_delta_6h",
    "vib_delta_6h",
]


# ---------- 2. Request schema (one field per feature) ----------
class SensorReading(BaseModel):
    machine_id: int
    temperature: float
    vibration: float
    pressure: float
    current: float
    rpm: float
    status_code: int
    temp_mean_6h: float
    temp_std_6h: float
    vib_mean_6h: float
    vib_std_6h: float
    temp_mean_12h: float
    temp_std_12h: float
    vib_mean_12h: float
    vib_std_12h: float
    temp_mean_24h: float
    temp_std_24h: float
    vib_mean_24h: float
    vib_std_24h: float
    temp_delta_1h: float
    vib_delta_1h: float
    temp_delta_6h: float
    vib_delta_6h: float


# ---------- 3. FastAPI app ----------
app = FastAPI(
    title="Predictive Maintenance API",
    version="1.0.0",
    description="Predict failures within 72 hours using sensor features.",
)


# ---------- 4. Load trained model pipeline ----------
PROJECT_ROOT = Path(__file__).resolve().parents[2]
MODEL_PATH = PROJECT_ROOT / "models" / "best_model.pkl"

model = joblib.load(MODEL_PATH)


# ---------- 5. Routes ----------
@app.get("/")
def root():
    return {"message": "Predictive Maintenance API is running."}


@app.post("/predict")
def predict(reading: SensorReading):
    """
    Take 24h/12h/6h sensor summary features and return failure risk.
    """
    try:
        data = reading.dict()
        # DataFrame with correct column order
        df = pd.DataFrame([data])[FEATURES]

        proba = float(model.predict_proba(df)[0, 1])
        label = int(proba >= 0.5)

        return {
            "failure_within_72h": label,
            "failure_probability": round(proba, 4),
        }

    except Exception as e:
        # helpful debug info instead of plain "Internal Server Error"
        return {
            "error": str(e),
            "note": "Exception occurred while running prediction.",
        }
