from flask import Blueprint, request, jsonify
from models.Clusters.clusters import daily_hours_addicted_age_relation

cluster_bp = Blueprint('cluster_bp', __name__)

@cluster_bp.route('/predict/daily_hours_addicted_age_relation', methods=['GET'])
def predict_daily_hours_addicted_age_relation():
    result = daily_hours_addicted_age_relation()
    return jsonify({
        "plot_base64": result["plot"]
    })
    