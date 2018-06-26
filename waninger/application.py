# -*- coding: utf-8 -*-
"""Flask Application Factory

This module implements the flask application, blueprints, and routes.
"""

from flask import (
    Flask, Blueprint, render_template
)

BP = Blueprint(
    'default', __name__,
    template_folder='templates',
    static_folder='static'
)


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


application = Flask(__name__)
application.register_blueprint(BP)

if __name__ == '__main__':
    application.run()
