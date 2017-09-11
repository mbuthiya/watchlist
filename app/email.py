from flask_mail import Message
from flask import render_template
from . import mail
subject_pref = None
sender_email = None

def configure_request(app):
    global subject_line,sender_email
    subject_pref = app.config['SUBJECT_PREFIX']
    sender_email = app.config['SENDER_EMAIL']


def mail_message(subject,template,to,**kwargs):
    email = Message(subject_pref+subject,sender=sender_email,recipients=[to]))
    email.body= render_template(template + ".txt",**kwargs)
    email.html = render_template(template + ".html",**kwargs)
    mail.send(email)
