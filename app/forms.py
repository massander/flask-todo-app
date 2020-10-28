from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, ValidationError
from wtforms.validators import InputRequired, Length, NumberRange

class CreateForm(FlaskForm):
    subject = StringField('Subject', validators = [InputRequired(), Length(min=3, max=25)])
    content = TextAreaField('Task', validators =[InputRequired()])
    deadline = StringField('Deadline', validators = [InputRequired(), Length(min=3, max=25)])