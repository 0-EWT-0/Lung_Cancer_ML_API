from flask import Blueprint, request, jsonify
from models.Linear_Regresions.linear_regresions import slepp_hours_affect_mental_health, social_media_addiction_conflicts, less_sleep_more_social_media, social_media_mental_health

linear_bp = Blueprint('linear_bp', __name__)

@linear_bp.route('/predict/avg_daily_usage_hours', methods=['POST'])
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

@linear_bp.route('/predict/social_media_mental_health', methods=['POST'])
def predict_social_media_mental_health():
    try:
        data = request.json
        avg_daily_usage_hours = data.get("avg_daily_usage_hours")
        addicted_score = data.get("addicted_score")
        if avg_daily_usage_hours is None or addicted_score is None:
            return jsonify({"error": "Faltan parámetros: avg_daily_usage_hours y addicted_score son requeridos"}), 400
        result = social_media_mental_health(float(avg_daily_usage_hours), float(addicted_score))
        return jsonify({
            "prediction_mental_health": result["prediction_mental_health"],
            "prediction_conflicts": result["prediction_conflicts"],
            "plot_base64": result["plot_base64"],
            "coefficient_mental": result["coefficient_mental"],
            "coefficient_conflicts": result["coefficient_conflicts"]
        }), 200
    except Exception as e:
        return jsonify({"error": f"Error en la predicción: {str(e)}"}), 500

