CROP_ADVISORY = {
    "Rice": {
        "fertilizer": "NPK 90:40:40",
        "irrigation": "Frequent flooding",
        "sowing_season": "Kharif"
    },
    "Maize": {
        "fertilizer": "NPK 120:60:40",
        "irrigation": "Every 7–10 days",
        "sowing_season": "Kharif / Rabi"
    },
    "Muskmelon": {
        "fertilizer": "NPK 60:50:50",
        "irrigation": "Every 7 days",
        "sowing_season": "Zaid"
    },
    "Watermelon": {
        "fertilizer": "NPK 80:60:60",
        "irrigation": "Every 6–8 days",
        "sowing_season": "Zaid"
    }
}

def get_crop_advisory(crop_name: str):
    return CROP_ADVISORY.get(
        crop_name,
        {
            "fertilizer": "Standard NPK",
            "irrigation": "As required",
            "sowing_season": "Depends on region"
        }
    )
