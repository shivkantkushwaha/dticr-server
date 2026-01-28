
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.schemas import CropInput
from app.utils.predictor import predict_crop_with_details
from app.utils.advisory import get_crop_advisory


# Initialize FastAPI app
app = FastAPI(
    title="AI-Based Crop Recommendation API",
    description="Recommends best crop based on soil and weather conditions",
    version="1.0"
)

# CORS Middleware (IMPORTANT for frontend connection)
app.add_middleware(
    CORSMiddleware,
    #allow_origins=["http://localhost:3000"],  # Next.js frontend
    allow_origins=["*"],  # TEMP for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check / Home route
@app.get("/")
def home():
    return {"message": "Crop Recommendation API is running"}

# Prediction route
@app.post("/predict")
def predict(data: CropInput):
    input_data = [
        data.nitrogen,
        data.phosphorus,
        data.potassium,
        data.temperature,
        data.humidity,
        data.rainfall,
        data.ph
    ]

    (
        recommended_crop,
        confidence,
        top_alternatives,
        suitability
    ) = predict_crop_with_details(input_data)

    advisory = get_crop_advisory(recommended_crop)

    return {
        "recommended_crop": recommended_crop,
        "confidence": round(confidence, 2),
        "top_alternatives": top_alternatives,
        "suitability": suitability,
        "advisory": advisory
    }
