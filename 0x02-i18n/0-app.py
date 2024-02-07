#!/usr/bin/env python3
"""
This is the first flask app module
"""
from flask import Flask
from routes.routes_0 import app_routes


def create_app():
    '''
    This creates flask app
    '''
    app = Flask(__name__)
    app.register_blueprint(app_routes)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
