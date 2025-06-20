from flask import Flask
from flask_cors import CORS
from services.processing import prepare_dataset
from controllers.logical_controller import logical_bp
from controllers.linear_controller import linear_bp
from controllers.tree_controller import tree_bp
from controllers.cluster_controller import cluster_bp
from controllers.correlation_controler import correlation_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(logical_bp)
app.register_blueprint(linear_bp)
app.register_blueprint(tree_bp)
app.register_blueprint(cluster_bp)
app.register_blueprint(correlation_bp)

@app.route('/')
def home():
    return '¡Flask está funcionando correctamente!'

if __name__ == '__main__':
    app.run(debug=True)
