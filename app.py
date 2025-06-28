from flask import Flask
from flask_cors import CORS
import os

from services.processing import prepare_dataset
from controllers.logical_controller import logical_bp
from controllers.linear_controller import linear_bp
from controllers.tree_controller import tree_bp
from controllers.cluster_controller import cluster_bp
from controllers.correlation_controler import correlation_bp
from controllers.boxplot_controller import boxplot_bp
from controllers.histogram_controller import histogram_bp
from controllers.user_controller import data_bp

app = Flask(__name__)
CORS(app)

# Registrar los blueprints
app.register_blueprint(logical_bp)
app.register_blueprint(linear_bp)
app.register_blueprint(tree_bp)
app.register_blueprint(cluster_bp)
app.register_blueprint(correlation_bp)
app.register_blueprint(boxplot_bp)
app.register_blueprint(histogram_bp)
app.register_blueprint(data_bp)

@app.route('/')
def home():
    return '¡Flask está funcionando correctamente en Render!'

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
