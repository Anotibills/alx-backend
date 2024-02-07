#!/usr/bin/env python3
"""
This improves the get_locale function
"""
from typing import Union
from flask import Flask, request
from flask_babel import Babel
from config import Config
from routes.routes_4 import app_routes


def create_app():
    '''
    This initialize babel with flask app
    '''
    app = Flask(__name__)
    babel = Babel(app)

    app.config.from_object(Config)
    app.register_blueprint(app_routes)

    @babel.localeselector
    def get_locale() -> Union[str, None]:
        '''
        This is the get locale configuration
        '''
        locale = request.args.get('locale')
        if locale and locale in Config.LANGUAGES:
            return locale
        return request.accept_languages.best_match(Config.LANGUAGES)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
