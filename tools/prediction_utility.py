import requests

def get_diabetes_prediction(pregnancies, glucose, bp, skin, insulin, bmi, dpf, age):
    api_url = "https://ayeshaaaa17-diabetes-prediction-api.hf.space/predict"
    
    # FIXED: The keys are now directly at the root level of the payload dictionary
    payload = {
        "Pregnancies": pregnancies,
        "Glucose": glucose,
        "BloodPressure": bp,
        "SkinThickness": skin,
        "Insulin": insulin,
        "BMI": bmi,
        "DiabetesPedigreeFunction": dpf,
        "Age": age
    }

    try:
        response = requests.post(api_url, json=payload, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        prediction = data.get("prediction", "Unknown")
        confidence = data.get("confidence", 0.0)
        
        return {"prediction": prediction, "confidence": confidence, "status": "success"}

    except Exception as error:
        return {"prediction": None, "confidence": 0.0, "status": "error", "message": str(error)}

if __name__ == "__main__":
    result = get_diabetes_prediction(6, 170, 156, 3, 134, 29, 2, 45)
    print("Test Result:")
    print(result)