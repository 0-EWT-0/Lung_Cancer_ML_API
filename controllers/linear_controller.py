from flask import Blueprint, request, jsonify
from models.Linear_Regresions.linear_regresions import slepp_hours_affect_mental_health, social_media_addiction_conflicts, less_sleep_more_social_media

linear_bp = Blueprint('linear_bp', __name__)

@linear_bp.route('/predict/Avg_Daily_Usage_Hours', methods=['POST'])
def predict_mental_health():
    data = request.json
    sleep_hours = float(data.get("sleep_hours"))
    mental_health_score = float(data.get("mental_health_score"))
    result = slepp_hours_affect_mental_health(sleep_hours, mental_health_score)
    return jsonify({
        "prediction": result["prediction"],
        "plot_base64": result["plot"]
    })

@linear_bp.route('/predict/social_media_addiction_conflicts', methods=['POST'])
def predict_social_media_addiction_conflicts():
    data = request.json
    addicted_score = float(data.get("addicted_score"))
    result = social_media_addiction_conflicts(addicted_score)
    return jsonify({
        "prediction": result["prediction"],
        "plot_base64": result["plot"]
    })

@linear_bp.route('/predict/less_sleep_more_social_media', methods=['POST'])
def predict_less_sleep_more_social_media():
    data = request.json
    media_hours = float(data.get("media_hours"))
    result = less_sleep_more_social_media(media_hours)
    return jsonify({
        "prediction": result["prediction"],
        "plot_base64": result["plot"]
    })