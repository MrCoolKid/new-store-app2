from flask import Blueprint,render_template,redirect,url_for,flash,request
from flask_login import login_required
from myproject import db
from myproject.models import Group
from myproject.admin.groups.forms import GroupForm,SearchForm

group_bp = Blueprint('groups',__name__,template_folder='templates/group')

@group_bp.route('/', methods=['GET','POST'])
@login_required
def group():
    page = request.args.get('page',1,type=int)
    grup = Group.query.order_by(Group.id.desc()).paginate(page=page,per_page=5)

    form = SearchForm()
    if form.validate_on_submit():
        grup_search= Group.query.filter(Group.groupname.like('%'+form.search.data+'%')).first()
        if not grup_search :
            flash('Your search not found!!!')
            return redirect(url_for('groups.group'))
        else:
            return redirect(url_for('groups.search',searchname=form.search.data))
    return render_template("admingroup.html",group_list=grup,form=form)

@group_bp.route('/search<searchname>', methods=['GET','POST'])
@login_required
def search(searchname):
    form = SearchForm()
    page = request.args.get('page',1,type=int)
    grup_search_list = Group.query.filter(Group.groupname.like('%'+searchname+'%')).order_by(Group.groupname.desc()).paginate(page=page,per_page=5)

    if form.validate_on_submit():
        grup_search = Group.query.filter(Group.groupname.like('%'+form.search.data+'%')).first()
        if not grup_search:
            flash('Your search not found!!!')
            return redirect(url_for('groups.group'))

        return redirect(url_for('groups.search',searchname=form.search.data))
    return render_template("groupsearch.html",form=form,searchname=searchname,group_search=grup_search_list)

@group_bp.route('/add', methods=['GET','POST'])
@login_required
def add():
    form = GroupForm()
    if form.validate_on_submit():
        cek = Group.query.filter_by(groupname=form.groupname.data).first()
        if not cek:
            grup = Group(groupname=form.groupname.data)
            db.session.add(grup)
            db.session.commit()
            flash("Product Group Added")
            return redirect(url_for('groups.group'))
        else:
            flash("Product Group Exist !!!")
            return redirect(url_for('groups.add'))

    return render_template("addgroups.html",form=form)

@group_bp.route('/edit/<int:group_id>', methods=['GET','POST'])
@login_required
def edit(group_id):
    grups = Group.query.filter_by(id=group_id).first()
    form = GroupForm()

    if form.validate_on_submit():
        cek = Group.query.filter_by(groupname=form.groupname.data).first()
        if not cek :
            grups.groupname = form.groupname.data
            db.session.commit()
            flash("Product Group has been Updated")
            return redirect(url_for('groups.group'))
        else:
            flash('Product Group not change or already exist!!!')
            return redirect(url_for('groups.edit',group_id=grups.id))

    elif request.method == 'GET':
        form.groupname.data = grups.groupname

    return render_template("editgroups.html",grup_select=grups, form=form)

@group_bp.route('/delete/<int:group_id>',methods=['GET','POST'])
@login_required
def delete(group_id):
    delete_grups = Group.query.filter_by(id=group_id).first()
    db.session.delete(delete_grups)
    db.session.commit()
    flash('Product Group has been deleted!!!')
    return redirect(url_for('groups.group'))
