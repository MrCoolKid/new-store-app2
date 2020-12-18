from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SelectField, SubmitField
from wtforms.validators import InputRequired,EqualTo,DataRequired



class SearchForm(FlaskForm):
    search = StringField('Search', validators=[InputRequired()])
    submit = SubmitField('Search')
