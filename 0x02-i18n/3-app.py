#!/usr/bin/env python3
"""
Get Locale From Request
"""

import babel
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Config Class setup
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEEL_DEFAULT_TIMEZONE = 'UTC'


app.comfig.from_object(Config)


@babel.localeselector
def get_locale():
    """
    Determine besst match with supported languages
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/', strict_slashes=False)
def index():
    """
    returns hello world
    """
    return render_template('3-index.html')

if __name__ == '__main__':
    app.run(debug=True)
