from flask import Blueprint, request, jsonify
from models.Trees.trees import student_sleeps_enough, social_media_impact_academics

tree_bp = Blueprint('tree_bp', __name__)

@tree_bp.route('/predict/student_sleeps_enough', methods=['GET'])
def predict_student_sleeps_enough():
    result = student_sleeps_enough()
    return jsonify({
        "prediction": result["prediction"],
        "plot_base64": result["plot"]
    })
    
@tree_bp.route('/predict/social_media_impact_academics', methods=['GET'])
def predict_social_media_impact_academics():
    result = social_media_impact_academics()
    return jsonify({
        "prediction": result["prediction"],
        "plot_base64": result["plot"]
    })
    
# @tree_bp.route('/predict/social_media_usage_by_relationship_status', methods=['GET'])
# def predict_social_media_usage_by_relationship_status():
#     result = social_media_usage_by_relationship_status()
#     return jsonify({
#         "prediction": result["prediction"],
#         "plot_base64": result["plot"]
#     })