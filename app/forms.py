from flask_wtf import Form
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class ReviewForm(Form):

    title = StringField('Review title',validators=[Required()])
    review = TextAreaField('Movie revie', validators=[Required()])
    submit = SubmitField('Submit')
