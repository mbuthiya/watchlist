subject_line = None
sender_email = None

def configure_request(app):
    global subject_line,sender_email
    subject_line = app.config['SUBJECT_PREFIX']
    sender_email = app.config['SENDER_EMAIL']
