from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required,Email

class ReviewForm(FlaskForm):

    title = StringField('Review title',validators=[Required()])
    review = TextAreaField('Movie review', validators=[Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    username = StringField('Username',validators = [Required()])
    email = StringField('Your Email Address',validators=[Required(),Email()])
    bio = StringField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
