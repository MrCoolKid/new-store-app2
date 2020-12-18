from flask import Blueprint,render_template,redirect,url_for,flash,request
from flask_login import login_required
from myproject import db,basedir
from myproject.core.views import harga
from myproject.models import Product,Group,Brand
from myproject.core.forms import SearchForm
from myproject.admin.products.forms import ProductForm,EditProductForm
from myproject.admin.products.picture_handler import add_product_pic
import os

product_bp = Blueprint('products',__name__,template_folder='templates/product')

@product_bp.route('/', methods=['GET','POST'])
@login_required
def product():
    page = request.args.get('page',1,type=int)
    product_list = Product.query.order_by(Product.id.desc()).paginate(page=page,per_page=5)

    form = SearchForm()
    if form.validate_on_submit():
        product_search = Product.query.filter(Product.name.like('%'+form.search.data+'%')).first()
        if not product_search:
            flash('Your search not found !!!')
            return redirect(url_for('products.product'))
        return redirect(url_for('products.search',searchname=form.search.data))
    return render_template("products.html",product_list=product_list,harga=harga,form=form)

@product_bp.route('/search<searchname>',methods=['GET','POST'])
@login_required
def search(searchname):
    page = request.args.get('page',1,type=int)
    product_search_list = Product.query.filter(Product.name.like('%'+searchname+'%')).order_by(Product.name.desc()).paginate(page=page,per_page=5)

    form = SearchForm()
    if form.validate_on_submit():
        product_search = Product.query.filter(Product.name.like('%'+form.search.data+'%')).first()
        if not product_search:
            flash('Your search not found !!!')
            return redirect(url_for('products.product'))
        return redirect(url_for('products.search',searchname=form.search.data))
    return render_template("productsearch.html",form=form,product_search=product_search_list,searchname=searchname,harga=harga)


@product_bp.route('/add', methods=['GET','POST'])
@login_required
def add():
    form = ProductForm()
    if form.validate_on_submit():
        cek = Product.query.filter_by(name=form.name.data).first()
        if not cek :
            product_photo = add_product_pic(form.photo.data, form.name.data)
            product = Product(name=form.name.data,price=form.price.data,
                              photo=product_photo,group_id=form.group.data.id,
                              brand_id=form.brand.data.id)
            db.session.add(product)
            db.session.commit()
            flash("Product Added")
            return redirect(url_for('products.product'))
        else:
            flash("Product Name Exist !!!")
            return redirect(url_for('products.add'))

    return render_template("addproducts.html",form=form)

@product_bp.route('/edit/<int:product_id>', methods=['GET','POST'])
@login_required
def edit(product_id):
    product_select = Product.query.filter_by(id=product_id).first()
    form = EditProductForm()
    if form.validate_on_submit():
        cek = Product.query.filter_by(name=form.name.data).first()

        if form.photo.data:
            pic = add_product_pic(form.photo.data, form.name.data)
            product_select.photo = pic

        product_select.name = form.name.data
        product_select.price = form.price.data
        db.session.commit()
        flash('Product updated!!!')
        return redirect(url_for('products.product'))

    elif request.method == "GET":
        form.name.data = product_select.name
        form.price.data = product_select.price
        form.photo.data = product_select.photo

    photo_produk= url_for('static',filename='upload_products/'+product_select.photo)
    return render_template('editproducts.html',form=form,foto=photo_produk,product_select=product_select)

@product_bp.route('/delete/<int:product_id>',methods=['GET','POST'])
@login_required
def delete(product_id):
    product_delete = Product.query.filter_by(id=product_id).first()
    filepath = os.path.join(basedir,'static/upload_products/'+product_delete.photo)
    db.session.delete(product_delete)
    db.session.commit()
    os.remove(filepath)
    flash('Product Deleted')
    return redirect(url_for('products.product'))
