from flask import (
    Flask, Blueprint, redirect, render_template, url_for
)

bp = Blueprint('default', __name__, url_prefix='/')


@bp.route('/')
def home():
    return render_template('index.html')


@bp.route('/about')
def about():
    return render_template('about.html')



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
