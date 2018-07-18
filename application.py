# -*- coding: utf-8 -*-
"""Flask Application Factory

This module implements the flask application, blueprints, and routes.
"""

from flask import Blueprint, Flask, render_template, send_from_directory
import numpy as np
import os


DEBUG = False

if DEBUG:
    try:
        from settings import load_environment
        load_environment()
    except:
        pass


BP = Blueprint(
    'default', __name__,
    template_folder='waninger/templates'
)


@BP.route('/downloads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    return send_from_directory(directory='static', filename=filename, as_attachment=True)


@BP.route('/')
def home():
    """register route to home"""
    result = dict(featured=f'/static/featured/{str(np.random.choice(len(os.listdir()), 1)[0]+1)}.jpg')
    return render_template('index.html', result=result)


@BP.route('/get_random_featured')
def get_random_featured():
    return f'/static/featured/{str(np.random.choice(len(os.listdir()), 1)[0]+1)}.jpg'


@BP.route('/projects')
def projects():
    """register route to projects"""
    return render_template('projects.html')


@BP.route('/resume')
def resume():
    """register route to resume"""
    return render_template('resume.html')


application = Flask(__name__)
application.register_blueprint(BP)

if __name__ == '__main__':
    application.run(debug=DEBUG)
