#!/usr/bin/env python3
"""
This creates a get_locale function with the babel.localeselector decorator
"""
from flask import Flask, request
from flask_babel import Babel
from routes.routes_2 import app_routes
from config import Config


def create_app():
    '''
    This initializes babel with flask app
    '''
    app = Flask(__name__)
    babel = Babel(app)

    app.config.from_object(Config)
    app.register_blueprint(app_routes)

    @babel.localeselector
    def get_locale() -> str:
        '''
        This determines the best match for supported languages
        '''
        return request.accept_languages.best_match(Config.LANGUAGES)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
