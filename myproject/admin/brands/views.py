from flask import Blueprint,render_template,redirect,url_for,flash,request
from flask_login import login_required
from myproject import db
from myproject.models import Brand
from myproject.admin.brands.forms import BrandForm

brand_bp = Blueprint('brands',__name__,template_folder='templates/brand')


@brand_bp.route('/')
@login_required
def brand():
    page = request.args.get('page',1,type=int)
    brand_list = Brand.query.order_by(Brand.id.desc()).paginate(page=page,per_page=5)
    return render_template("brands.html",brand_list=brand_list)

@brand_bp.route('/add',methods=['GET','POST'])
@login_required
def add():
    form = BrandForm()
    if form.validate_on_submit():
        cek = Brand.query.filter_by(brandname=form.brandname.data).first()
        if not cek :
            addbrand = Brand(brandname=form.brandname.data)
            db.session.add(addbrand)
            db.session.commit()
            flash('Product Brand Added')
            return redirect(url_for('brands.brand'))
        else :
            flash('Product Brand exist !!!')
            return redirect(url_for('brands.add'))
    return render_template("addbrands.html",form=form)

@brand_bp.route('/edit/<int:brand_id>',methods=['GET','POST'])
@login_required
def edit(brand_id):
    brand_select = Brand.query.filter_by(id=brand_id).first()
    form = BrandForm()
    if form.validate_on_submit():
        cek = Brand.query.filter_by(brandname=form.brandname.data).first()
        if not cek :
            brand_select.brandname = form.brandname.data
            db.session.commit()
            flash('Product Brand Updated')
            return redirect(url_for('brands.brand'))
        else:
            flash('Product Brand is not change or Exist !!!')
            return redirect(url_for('brands.edit',brand_id=brand_select.id))

    elif request.method == 'GET':
        form.brandname.data = brand_select.brandname

    return render_template("editbrands.html",form=form,brand_select=brand_select)

@brand_bp.route('/delete/<int:brand_id>',methods=['GET','POST'])
@login_required
def delete(brand_id):
    brand_delete = Brand.query.filter_by(id=brand_id).first()
    db.session.delete(brand_delete)
    db.session.commit()
    flash('Product Brand deleted!!!')
    return redirect(url_for('brands.brand'))
