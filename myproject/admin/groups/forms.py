from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired,DataRequired


class GroupForm(FlaskForm):
    groupname = StringField('Nama Group',validators=[InputRequired()])
    submit = SubmitField('Submit')

class SearchForm(FlaskForm):
    search= StringField(validators=[DataRequired()])
    submit = SubmitField('Submit')
