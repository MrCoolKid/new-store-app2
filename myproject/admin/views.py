from flask import render_template,Blueprint,redirect,url_for,request,flash
from flask_login import login_required
from flask_login import login_user,logout_user
from myproject.models import User
from myproject.admin.forms import LoginForm


admin_bp = Blueprint('admin',__name__,template_folder='templates')

@admin_bp.route('/')
@login_required
def admin():
    return render_template("admin.html")


@admin_bp.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Log in Success')

            next = request.args.get('next')
            if next == None or not next[0] == '/adm2':
                next = url_for('admin.admin')
                return redirect(next)
        else:
            flash("User not found or wrong Password!")
            return redirect(url_for('admin.login'))
    return render_template('accounts/login.html',form=form)


@admin_bp.route('/logout')
def logout():
    logout_user()
    flash('you are logout now')
    return redirect(url_for('admin.login'))
