from flask import Blueprint, request, jsonify
from models.Histograms.histograms import daily_usage_hours_histogram, age_histogram, sleep_hours_histogram

histogram_bp = Blueprint('histogram_bp', __name__)

@histogram_bp.route('/predict/daily_usage_hours_histogram', methods=['GET'])
def predict_daily_usage_hours_histogram():
    result = daily_usage_hours_histogram()
    return jsonify({
        "plot_base64": result["plot"]
    })
    
@histogram_bp.route('/predict/age_histogram', methods=['GET'])
def predict_age_histogram():
    result = age_histogram()
    return jsonify({
        "plot_base64": result["plot"]
    })
    
@histogram_bp.route('/predict/sleep_hours_histogram', methods=['GET'])
def predict_sleep_hours_histogram():
    result = sleep_hours_histogram()
    return jsonify({
        "plot_base64": result["plot"]
    })