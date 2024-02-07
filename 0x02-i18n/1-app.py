#!/usr/bin/env python3
"""
This is the module that initiaze babel with flask app
"""
from flask import Flask
from flask_babel import Babel
from routes.routes_1 import app_routes


def create_app():
    '''
    This initiate babel with flask app
    '''
    app = Flask(__name__)
    babel = Babel(app)

    class Config(object):
        '''
        This is the configuration class for babel
        '''
        LANGUAGES = ["en", "fr"]
        BABEL_DEFAULT_LOCALE = 'en'
        BABEL_DEFAULT_TIMEZONE = 'UTC'

    app.config.from_object(Config)
    app.register_blueprint(app_routes)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
