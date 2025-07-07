from flask import Blueprint, request, jsonify
from models.Boxplots.boxplots import usage_by_relationship_status_boxplot, mental_health_by_usage_boxplot

boxplot_bp = Blueprint('boxplot_bp', __name__)

@boxplot_bp.route('/predict/mental_health_by_usage_boxplot', methods=['GET'])
def predict_mental_health_by_usage_boxplot():
    result = mental_health_by_usage_boxplot()
    return jsonify({
        "plot_base64": result["plot"],
        "data_points": result["data"]
    })

@boxplot_bp.route('/predict/usage_by_relationship_status_boxplot', methods=['GET'])
def predict_usage_by_relationship_status_boxplot():
    result = usage_by_relationship_status_boxplot()
    return jsonify({
        "plot_base64": result["plot"],
        "data_points": result["data"]
    })

