from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SelectField
from wtforms.validators import InputRequired,EqualTo,DataRequired



class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
