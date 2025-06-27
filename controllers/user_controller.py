from flask import Blueprint, request, jsonify
from services.user.user_service import insert_user_data, get_data_by_username
from services.user.prepare_user_data import predict_user_results 

data_bp = Blueprint('data_bp', __name__)

@data_bp.route('/data', methods=['POST'])
def create_data():
    try:
        user_data = request.json

        predicciones = predict_user_results(
            sleep_hours=float(user_data['Sleep_Hours_Per_Night']),
            avg_usage=float(user_data['Avg_Daily_Usage_Hours'])
        )
        
        user_data['Addicted_Score'] = predicciones['addicted_score']
        user_data['Affects_Academic_Performance'] = predicciones['affects_academic']
        user_data['Mental_Health_Score'] = predicciones['mental_health']

        new_id = insert_user_data(user_data)

        return jsonify({
            "message": "Datos insertados correctamente",
            "data_id": new_id,
            "usuario": user_data,
            "predictions": {
                "Addicted_Score": predicciones['addicted_score'],
                "Affects_Academic_Performance": predicciones['affects_academic'],
                "Mental_Health_Score": predicciones['mental_health'],
            },
            "graphs": predicciones['graphs']
        }), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@data_bp.route('/data/<username>', methods=['GET'])
def get_user_data(username):
    try:
        data_list = get_data_by_username(username)
        if not data_list:
            return jsonify({"message": "Usuario no encontrado"}), 404

        user = data_list[0] 

        predicciones = predict_user_results(
            sleep_hours=float(user['Sleep_Hours_Per_Night']),
            avg_usage=float(user['Avg_Daily_Usage_Hours'])
        )

        return jsonify({
            "usuario": user,
            "predictions": {
                "Addicted_Score": predicciones['addicted_score'],
                "Affects_Academic_Performance": predicciones['affects_academic'],
                "Mental_Health_Score": predicciones['mental_health']
            }
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400

