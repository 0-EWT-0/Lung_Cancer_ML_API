from flask import Blueprint, request, jsonify
from models.Correlations.correlations import daily_usage_addiction_conflicts_sleep_correlation

correlation_bp = Blueprint('correlation_bp', __name__)

@correlation_bp.route('/predict/daily_usage_addiction_conflicts_sleep_correlation', methods=['GET'])
def predict_daily_usage_addiction_conflicts_sleep_correlation():
    result = daily_usage_addiction_conflicts_sleep_correlation()
    return jsonify({
        "plot_base64": result["plot"]
    })