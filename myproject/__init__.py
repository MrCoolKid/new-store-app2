from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SECRET_KEY'] = 'mysecretkeyyes'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://gunawan:Belajar2020@192.168.100.99/hadi_produk_list'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
Migrate(app,db)


#flask-login
login_manager = LoginManager(app)
login_manager.login_view = "admin.login"


##BLUEPRINT
from myproject.core.views import core
from myproject.admin.views import admin_bp
from myproject.admin.users.views import users_bp
from myproject.admin.groups.views import group_bp
from myproject.admin.brands.views import brand_bp
from myproject.admin.products.views import product_bp


app.register_blueprint(core)
app.register_blueprint(admin_bp,url_prefix='/adm2')
app.register_blueprint(users_bp,url_prefix='/adm2/users')
app.register_blueprint(group_bp,url_prefix='/adm2/groups')
app.register_blueprint(brand_bp,url_prefix='/adm2/brands')
app.register_blueprint(product_bp,url_prefix='/adm2/products')
