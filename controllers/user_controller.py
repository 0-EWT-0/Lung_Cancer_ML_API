from flask import Blueprint, request, jsonify
from services.user.user_service import insert_user_data
from services.user.prepare_user_data import predict_user_results 

data_bp = Blueprint('data_bp', __name__)

@data_bp.route('/data', methods=['POST'])
def create_data():
    try:
        user_data = request.json

        predicciones = predict_user_results(
            sleep_hours=float(user_data['sleep_hours_per_night']),
            avg_usage=float(user_data['avg_daily_usage_hours'])
        )
        
        user_data['addicted_score'] = predicciones['addicted_score']
        user_data['affects_academic_performance'] = predicciones['affects_academic']
        user_data['mental_health_score'] = predicciones['mental_health']

        new_id = insert_user_data(user_data)

        return jsonify({
            "message": "Datos insertados correctamente",
            "student_id": new_id,
            "usuario": user_data,
            "predictions": {
                "addicted_score": predicciones['addicted_score'],
                "affects_academic_performance": predicciones['affects_academic'],
                "mental_health_score": predicciones['mental_health'],
            },
            "graphs": predicciones['graphs']
        }), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
# @data_bp.route('/data/<username>', methods=['GET'])
# def get_user_data(username):
#     try:
#         data_list = get_data_by_username(username)
#         if not data_list:
#             return jsonify({"message": "Usuario no encontrado"}), 404

#         user = data_list[0] 

#         predicciones = predict_user_results(
#             sleep_hours=float(user['sleep_hours_per_night']),
#             avg_usage=float(user['avg_daily_usage_hours'])
#         )

#         return jsonify({
#             "usuario": user,
#             "predictions": {
#                 "addicted_score": predicciones['addicted_score'],
#                 "affects_academic_performance": predicciones['affects_academic'],
#                 "mental_health_score": predicciones['mental_health']
#             }
#         }), 200

#     except Exception as e:
#         return jsonify({"error": str(e)}), 400

