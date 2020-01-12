from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_wtf.file import FileField, FileRequired


class SubmitTextForm(FlaskForm):
    name = StringField('name')
    file = FileField('file', validators=[FileRequired()])
    submit = SubmitField('submit')
