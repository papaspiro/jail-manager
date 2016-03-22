# Import flask dependencies
from flask import Blueprint, request, render_template
from flask import flash, g, session, redirect, url_for

#encryption helpers
from werkzeug import  check_password_hash , generate_password_hash

#import database object from main app module
from app import db

#module forms
from app.mod_auth.forms import LoginForm
from app.mod_auth.models  import User

#define blueprint
mod_auth = Blueprint('auth',__name__,url_prefix='/auth')

@mod_auth.route('/signin/',methods=['GET','POST'])
def signin():
	form = LoginForm(request.form)
	#verify the signin form
	if form.validate_on_submit():
		user = Userq.query.filter_by(email = form.email.data,password = form.password.data)
		if user and check_password_hash(user.password ,form.user.data):
			session['user_id'] = user
			flash('welcome %s' %user.name)
			#return redirect( url_for('auth.home success landing page'))
			return redirect( url_for('/index'))
		flash('wrong email address or password','error_message')

	return render_template("/auth/signin.html",form=form)