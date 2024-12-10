from flask import Flask
from controllers.search_controller import search_bp
from domain.kernel.config import Config

app = Flask(__name__)
app.register_blueprint(search_bp)

if __name__ == "__main__":
    app.run(debug=Config.DEBUG)