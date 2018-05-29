from flask import Blueprint,render_template,redirect,url_for,request,current_app,flash
from pymongo import ReturnDocument
from flask_login import login_user,logout_user,current_user,login_required

from ..app import mongo
from ..forms import RegisterForm,LoginForm
from ..users import register_user,validate_user


login = Blueprint('login',__name__)


@login.route('/login',methods=['GET','POST'])
def login_page():

	# if user is already logged in, redirect to index page
	if current_user.is_authenticated:
		return redirect(url_for('hello.index_page'))

	form = LoginForm()
	
	cred_error = False
	if form.validate_on_submit():
		# check user's existence/credentials
		user = validate_user(form.username.data,form.passwd.data)
		if user:
			login_user(user)
			
			# check if next parameter dictates specific redirect
			next = request.args.get('next')
			# IMPORTANT NOTE: next must be checked for open redirect attempts!
			# Python's urlparse can be tricked to perceive an external redirect as an internal one!
			# Here we check that next string starts exactly with /APP_PREFIX/
			if next and next.startswith(current_app.config['REDIRECT_PREFIX']):
				return redirect(next) 
			
			# no next parameter or next parameter has illegal value
			return redirect(url_for('hello.index_page'))
	
		# user provided invalid credentials
		cred_error = True
		
	return render_template('login.html',form=form,cred_error=cred_error)


@login.route('/register',methods=['GET','POST'])
def register_page():

	# if user is already logged in, redirect to index page
	if current_user.is_authenticated:
		return redirect(url_for('hello.index_page'))

	form = RegisterForm()
	
	if form.validate_on_submit():
		# register new user
		user = register_user(form.username.data,form.passwd.data)
		# if registration ok (should nornally be), log the new user in
		if user is not None:
			login_user(user)
			# redirect to index page
			return redirect(url_for('hello.index_page'))
	
	return render_template('register.html',form=form)


@login.route('/logout')
@login_required
def logout_page():
	logout_user()
	return redirect(url_for('login.login_page'))

