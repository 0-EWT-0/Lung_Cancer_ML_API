from flask import Blueprint, request, jsonify
from models.Linear_Regresions.linear_regresions import slepp_hours_affect_mental_health, social_media_addiction_conflicts, less_sleep_more_social_media, social_media_mental_health

linear_bp = Blueprint('linear_bp', __name__)

@linear_bp.route('/predict/sleep_mental_health', methods=['POST'])
def predict_sleep_mental_health():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No se proporcionaron datos en la solicitud"}), 400

        sleep_hours = data.get("sleep_hours")
        mental_health_score = data.get("mental_health_score")

        if sleep_hours is None or mental_health_score is None:
            return jsonify({"error": "Faltan parámetros: sleep_hours y mental_health_score son requeridos"}), 400

        try:
            sleep_hours = float(sleep_hours)
            mental_health_score = float(mental_health_score)
            if sleep_hours < 0 or mental_health_score < 0:
                return jsonify({"error": "Los parámetros no pueden ser negativos"}), 400
        except (ValueError, TypeError):
            return jsonify({"error": "Los parámetros deben ser valores numéricos"}), 400

        result = slepp_hours_affect_mental_health(sleep_hours, mental_health_score)
        return jsonify({
            "prediction": result["prediction"],
            "plot_base64": result["plot"]
        }), 200

    except Exception as e:
        return jsonify({"error": f"Error en la predicción: {str(e)}"}), 500

@linear_bp.route('/predict/social_media_addiction_conflicts', methods=['POST'])
def predict_social_media_addiction_conflicts():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No se proporcionaron datos en la solicitud"}), 400

        addicted_score = data.get("addicted_score")
        if addicted_score is None:
            return jsonify({"error": "Falta el parámetro: addicted_score es requerido"}), 400

        try:
            addicted_score = float(addicted_score)
            if addicted_score < 0:
                return jsonify({"error": "addicted_score no puede ser negativo"}), 400
        except (ValueError, TypeError):
            return jsonify({"error": "addicted_score debe ser un valor numérico"}), 400

        result = social_media_addiction_conflicts(addicted_score)
        return jsonify({
            "prediction": result["prediction"],
            "plot_base64": result["plot"],
            "coefficient": result["coefficient"]
        }), 200

    except Exception as e:
        return jsonify({"error": f"Error en la predicción: {str(e)}"}), 500

@linear_bp.route('/predict/less_sleep_more_social_media', methods=['POST'])
def predict_less_sleep_more_social_media():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No se proporcionaron datos en la solicitud"}), 400

        media_hours = data.get("media_hours")
        if media_hours is None:
            return jsonify({"error": "Falta el parámetro: media_hours es requerido"}), 400

        try:
            media_hours = float(media_hours)
            if media_hours < 0:
                return jsonify({"error": "media_hours no puede ser negativo"}), 400
        except (ValueError, TypeError):
            return jsonify({"error": "media_hours debe ser un valor numérico"}), 400

        result = less_sleep_more_social_media(media_hours)
        return jsonify({
            "prediction": result["prediction"],
            "plot_base64": result["plot"]
        }), 200

    except Exception as e:
        return jsonify({"error": f"Error en la predicción: {str(e)}"}), 500

@linear_bp.route('/predict/social_media_mental_health', methods=['POST'])
def predict_social_media_mental_health():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No se proporcionaron datos en la solicitud"}), 400

        avg_daily_usage_hours = data.get("avg_daily_usage_hours")
        if avg_daily_usage_hours is None:
            return jsonify({"error": "Falta el parámetro: avg_daily_usage_hours es requerido"}), 400

        try:
            avg_daily_usage_hours = float(avg_daily_usage_hours)
            if avg_daily_usage_hours < 0:
                return jsonify({"error": "avg_daily_usage_hours no puede ser negativo"}), 400
        except (ValueError, TypeError):
            return jsonify({"error": "avg_daily_usage_hours debe ser un valor numérico"}), 400

        result = social_media_mental_health(avg_daily_usage_hours)
        return jsonify({
            "prediction": result["prediction"],
            "plot_base64": result["plot"],
            "coefficient": result["coefficient"]
        }), 200

    except Exception as e:
        return jsonify({"error": f"Error en la predicción: {str(e)}"}), 500