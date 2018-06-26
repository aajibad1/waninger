# -*- coding: utf-8 -*-
"""Flask Application Factory

This module implements the flask application, blueprints, and routes.
"""

from flask import (
    Flask, Blueprint, render_template
)

BP = Blueprint('default', __name__, template_folder='waninger/templates')


@BP.route('/')
def home():
    """register route to home"""
    return render_template('index.html')


@BP.route('/projects')
def projects():
    """register route to projects"""
    return render_template('projects.html')


@BP.route('/resume')
def resume():
    """register route to resume"""
    return render_template('resume.html')


@BP.route('/contact')
def contact():
    """register route to contact form"""
    return render_template('contact.html')


def create_app(test_config=None):
    """generate the application"""
    app = Flask(__name__, instance_relative_config=True)

    # load the app config
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    app.register_blueprint(BP)

    return app


if __name__ == '__main__':
    create_app().run()
