from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    phonenumber = StringField('Phone Number', validators=[DataRequired()])
    submit = SubmitField()


class DeletePostForm(FlaskForm):
    submit = SubmitField()