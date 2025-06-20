
from flask import Blueprint, request, jsonify
from models.Logical_Regresions.logical_regresions import single_more_hours_social_media, relations_affect_academy_preformance, less_sleep_in_complicated_relationship

logical_bp = Blueprint('logical_bp', __name__)

@logical_bp.route('/predict/single_status', methods=['POST'])
def predict_single_status():
    data = request.json
    hours = float(data.get("hours"))
    result = single_more_hours_social_media(hours)
    return jsonify({
        "prediction": result["prediction"],
        "plot_base64": result["plot"]
    })

@logical_bp.route('/predict/academic_impact', methods=['POST'])
def predict_academic_impact():
    data = request.json
    is_in_relationship = bool(data.get("is_in_relationship"))
    result = relations_affect_academy_preformance(is_in_relationship)
    return jsonify({
        "prediction": result["prediction"],
        "plot_base64": result["plot"]
    })

@logical_bp.route('/predict/less_sleep_relation', methods=['POST'])
def predict_less_sleep_relation():
    data = request.json
    sleep_hours = int(data.get("sleep_hours"))
    result = less_sleep_in_complicated_relationship(sleep_hours)
    return jsonify({
        "prediction": result["prediction"],
        "plot_base64": result["plot"]
    })