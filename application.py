# -*- coding: utf-8 -*-
"""Flask Application Factory

This module implements the flask application, blueprints, and routes.
"""

from email.mime.text import MIMEText
from flask import Blueprint, Flask, render_template, request
import numpy as np
import os
import smtplib
from wtforms import Form, StringField, SubmitField, TextAreaField, validators


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


class ContactForm(Form):
    name = StringField('Name', validators=[validators.DataRequired()])

    email = StringField('Email', validators=[
        validators.DataRequired(),
        validators.Email(),
        validators.Length(min=6, max=35)
    ])

    phone = StringField('Phone', validators=[
        validators.Length(min=5, max=17),
        validators.Optional()
    ])

    message = TextAreaField('Message', validators=[validators.DataRequired()])
    submit = SubmitField('Submit')


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


@BP.route('/contact', methods=['GET', 'POST'])
def contact():
    """register route to contact form"""
    form = ContactForm(request.form)

    if request.method == 'GET':
        return render_template('contact.html', form=form)

    elif request.method == 'POST' and form.validate():
        form = request.form

        text = f'name: {form["name"]}\n' \
               f'phone: {form["phone"]}\n' \
               f'email: {form["email"]}\n' \
               f'message:\n{form["message"]}'

        send_mail(text, form["email"])
        return thanks()

    else:
        return render_template('contact.html', form=form)


@BP.route('/thanks')
def thanks():
    return render_template('thanks.html')


def send_mail(text, to):
    msg = MIMEText(text)
    msg['Subject'] = 'resume contact'
    msg['From'] = os.environ['SMTP_EMAIL']
    msg['To'] = to

    # start a session
    session = smtplib.SMTP(
        os.environ['SMTP_GATEWAY'],
        os.environ['SMTP_PORT']
    )

    # initiate TLS and login
    session.starttls()
    session.login(
        os.environ['SMTP_EMAIL'],
        os.environ['SMTP_PASSWORD']
    )

    # send the email
    session.sendmail(
        os.environ['SMTP_EMAIL'],
        to,
        msg.as_string()
    )


application = Flask(__name__)
application.register_blueprint(BP)

if __name__ == '__main__':
    application.run(debug=DEBUG)
