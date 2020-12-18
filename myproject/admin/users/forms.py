from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SelectField
from wtforms.validators import InputRequired,EqualTo,DataRequired




class AdduserForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    role = SelectField('Role',choices=[('admin','admin'),('standard','standard')])
    password = PasswordField('Password', validators=[DataRequired(),EqualTo('confirm_password',message='Password must match!!!')])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])


class EdituserForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    role = SelectField('Role',choices=[('admin','admin'),('standard','standard')])

class PasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired(),EqualTo('confirm_password',message='Password must match!!!')])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])
