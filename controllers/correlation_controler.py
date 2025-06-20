from flask import Blueprint, request, jsonify
from models.Correlations.correlations import daily_usage_addiction_conflicts_sleep_correlation, general_correlation_matrix

correlation_bp = Blueprint('correlation_bp', __name__)

@correlation_bp.route('/predict/daily_usage_addiction_conflicts_sleep_correlation', methods=['GET'])
def predict_daily_usage_addiction_conflicts_sleep_correlation():
    result = daily_usage_addiction_conflicts_sleep_correlation()
    return jsonify({
        "plot_base64": result["plot"]
    })
    
@correlation_bp.route('/predict/general_correlation_matrix', methods=['GET'])
def predict_general_correlation_matrix():
    result = general_correlation_matrix()
    return jsonify({
        "plot_base64": result["plot"]
    })