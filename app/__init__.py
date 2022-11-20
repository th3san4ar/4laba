from flask import Flask
from .views import blueprints


def create_app():
    app = Flask(__name__)

    for bp in blueprints:
        app.register_blueprint(bp)

    return app