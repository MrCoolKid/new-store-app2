from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,IntegerField
from wtforms.validators import InputRequired,DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from flask_wtf.file import FileField,FileAllowed
from myproject.models import Group,Brand

def group_list():
    return Group.query

def brand_list():
    return Brand.query

class ProductForm(FlaskForm):
    group = QuerySelectField('Group Name',query_factory=group_list,allow_blank=False,get_label='groupname')
    brand = QuerySelectField('Brand Name',query_factory=brand_list,allow_blank=False,get_label='brandname')
    name = StringField('Product Name',validators=[InputRequired()])
    photo = FileField('Product Photo',validators=[InputRequired(),FileAllowed(['jpg','png','jpeg'],message="File must be jpg, png or jpeg!")])
    photo = FileField('Product Photo',validators=[InputRequired(),FileAllowed(['jpg','png','jpeg'])])
    price = IntegerField('Product Price',validators=[InputRequired()])

class EditProductForm(FlaskForm):
    name = StringField('Product Name', validators=[InputRequired()])
    photo = FileField('Product Photo',validators=[FileAllowed(['jpg','png','jpeg'])])
    price = IntegerField('Product Price',validators=[InputRequired()])
