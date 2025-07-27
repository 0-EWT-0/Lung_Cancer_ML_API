# controllers/prediction_controller.py
from flask import Blueprint, request, jsonify
from models.Predictions.predictions import predict_survival

prediction_bp = Blueprint('prediction_bp', __name__)

@prediction_bp.route('/predict/lung_cancer_survival', methods=['POST'])
def predict_lung_cancer_survival():
    try:
        data = request.get_json()
        result = predict_survival(
            smoking_status=int(data["smoking_status"]),
            family_history=int(data["family_history"]),
            bmi=float(data["bmi"]),
            cholesterol_level=int(data["cholesterol_level"]),
            country=str(data["country"]) if "country" in data else None,
            asthma=int(data["asthma"]),
            hypertension=int(data["hypertension"]),
            cirrhosis=int(data["cirrhosis"]),
            other_cancer=int(data["other_cancer"]),
            age=int(data["age"]),
            gender=int(data["gender"]),
            cancer_stage=int(data["cancer_stage"]) if "cancer_stage" in data else None,
            diagnosis_date=str(data["diagnosis_date"]) if "diagnosis_date" in data else None,
            treatment_type=int(data["treatment_type"]) if "treatment_type" in data else None,
            end_treatment_date=str(data["end_treatment_date"]) if "end_treatment_date" in data else None

        )
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 400
