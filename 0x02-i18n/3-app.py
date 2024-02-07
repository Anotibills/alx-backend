#!/usr/bin/env python3
"""
This configures the get_locale function
"""
from typing import Union
from flask import Flask, request
from flask_babel import Babel
from routes.routes_3 import app_routes
from config import Config


def create_app():
    '''
    This initialize the babel with flask app
    '''
    app = Flask(__name__)
    babel = Babel(app)

    app.config.from_object(Config)
    app.register_blueprint(app_routes)

    @babel.localeselector
    def get_locale() -> Union[str, None]:
        '''
        This is to configure the get locale
        '''
        return request.accept_languages.best_match(Config.LANGUAGES)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
