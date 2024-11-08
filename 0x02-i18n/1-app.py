#!/usr/bin/env python3
"""
Basic Basel Setup
"""

import babel
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Config class setup
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEEL_DEFAULT_TIMEZONE = 'UTC'


app.comfig.from_object(Config)


@app.route('/', strict_slashes=False)
def index():
    """
    returns hello world
    """
    return render_template('1-index.html')

if __name__ == '__main__':
    app.run(debug=True)
