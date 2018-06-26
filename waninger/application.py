from flask import (
    Flask, Blueprint, render_template
)

bp = Blueprint('default', __name__, template_folder='templates')


@bp.route('/')
def home():
    return render_template('index.html')


@bp.route('/projects')
def projects():
    return render_template('projects.html')


@bp.route('/resume')
def resume():
    return render_template('resume.html')


@bp.route('/contact')
def contact():
    return render_template('contact.html')


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    # load the app config
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    app.register_blueprint(bp)

    return app


if __name__ == '__main__':
    create_app().run()