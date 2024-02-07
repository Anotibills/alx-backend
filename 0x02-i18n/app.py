#!/usr/bin/env python3
"""
This is the main module
"""
from datetime import datetime
from flask_babel import Babel, _, format_datetime
from flask import Flask, render_template, request, g
import pytz
from typing import Union

app = Flask(__name__, template_folder='templates')
babel = Babel(app)


class Config(object):
    '''
    This is the configuration of class for Babel
    '''

    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[dict, None]:
    '''
    This returns a user dictionary
    '''

    try:
        login_as = request.args.get("login_as")
        user = users.get(int(login_as))
    except (ValueError, TypeError, KeyError):
        user = None

    return user


@app.before_request
def before_request():
    '''
    This is the operation that happens before any request
    '''
    user = get_user()
    g.user = user


@app.route('/', methods=['GET'], strict_slashes=False)
def hello_world() -> str:
    '''
    This renders a basic template for Babel Implementation
    '''
    timezone = get_timezone()
    current_time = datetime.now(pytz.timezone(timezone))
    current_time = format_datetime(current_time)
    return render_template("index.html", current_time=current_time)


@babel.localeselector
def get_locale() -> str:
    '''
    This select a language translation to use for that request
    '''
    locale = request.args.get("locale")
    if locale and locale in app.config['LANGUAGES']:
        return locale

    if g.user:
        locale = g.user.get("locale")
        if locale and locale in app.config['LANGUAGES']:
            return locale

    locale = request.headers.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    '''
    This finds timezone in URL parameters from user settings default to UTC
    '''
    try:
        timezone = request.args.get("timezone") or (g.user and g.user.get("timezone")) or app.config["BABEL_DEFAULT_TIMEZONE"]
        pytz.timezone(timezone)  # Verify timezone
    except pytz.UnknownTimeZoneError:
        timezone = "UTC"

    return timezone


if __name__ == "__main__":
    app.run()
