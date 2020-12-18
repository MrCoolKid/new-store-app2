from myproject import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

####MODELS######
class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),unique=True)
    password = db.Column(db.String(128))
    role = db.Column(db.String(64))

    def __init__(self,username,password,role):
        self.username = username
        self.password = generate_password_hash(password)
        self.role = role

    def check_password(self,password):
        return check_password_hash(self.password,password)

    def __repr__(self):
        return f"username:{self.username} role:{self.role}"


class Group(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    groupname = db.Column(db.String(64))

    products = db.relationship('Product',backref='grup',lazy=True)

    def __repr__(self):
        return f"groupname:{self.groupname}"


class Brand(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    brandname = db.Column(db.String(64))

    products = db.relationship('Product',backref='merek',lazy=True)

    def __repr__(self):
        return f"brandname:{self.brandname}"

class Product(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(128))
    price = db.Column(db.Integer)
    photo = db.Column(db.String(128))

    group_id = db.Column(db.Integer,db.ForeignKey('group.id'))
    brand_id = db.Column(db.Integer,db.ForeignKey('brand.id'))

    def __repr__(self):
        return f"Nama Produk:{self.name} -- Harga:{self.price} --group_id:{self.group_id} --brand_id:{self.brand_id}"

###MODELS###########
