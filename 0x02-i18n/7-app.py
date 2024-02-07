#!/usr/bin/env python3
"""
This defines a get_timezone function
"""
from flask import Flask, request, render_template, g
from flask_babel import Babel
from typing import Union
from pytz import timezone, UnknownTimeZoneError

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    '''
    This is the babel configuration setup
    '''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app.config.from_object(Config)


def get_user():
    '''
    This is the get user error handler
    '''
    try:
        return users.get(int(request.args.get('login_as')))
    except (TypeError, ValueError):
        return None


@babel.localeselector
def get_locale() -> Union[str, None]:
    '''
    This is get locale initiator
    '''
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    '''
    This gets timezone
    '''
    user = get_user()
    if user:
        locale = user['timezone']
    elif request.args.get('timezone'):
        locale = request.args.get('timezone')
    else:
        locale = app.config['BABEL_DEFAULT_TIMEZONE']

    try:
        return timezone(locale).zone
    except UnknownTimeZoneError:
        return None


@app.before_request
def before_request():
    '''
    This handles before request
    '''
    g.user = get_user()


@app.route('/')
def index() -> str:
    '''
    This is the index
    '''
    return render_template('7-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
