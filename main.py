from app import create_app
from app.controllers.search_controller import search_bp

app = create_app()
app.register_blueprint(search_bp)

if __name__ == "__main__":
    app.run(debug=True)
