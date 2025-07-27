from flask import Flask
from flask_cors import CORS
import os

from services.processing import prepare_dataset
from controllers.prediction_controller import prediction_bp

app = Flask(__name__)
CORS(app)

# Registrar los blueprints
app.register_blueprint(prediction_bp)

@app.route('/')
def home():
    return '¡Flask está funcionando correctamente en Render!'

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
