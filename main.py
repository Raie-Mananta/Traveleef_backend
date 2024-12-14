from flask import Flask
from app.controllers.search_controller import search_bp
from flask_cors import CORS
app = Flask(__name__)
app.register_blueprint(search_bp)
CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})

if __name__ == "__main__":
    app.run(debug=True)
