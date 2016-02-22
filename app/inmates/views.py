from app import app
from flask import render_template ,flash ,redirect


@app.route("/index")
def index():	
	user={"nickname":"nothing",'title':'impact'}
	return render_template("index.html",user=user,title="Nsawam Inmate MIS")	


#eg form view
@app.route('/login',methods=['GET','POST'])
def login():
	form = LoginForm()
	#true if form submission is successfuk
	if form.validate_on_submit():
		#do form processing
		flash("Login requested for OpenID = %s, remember_me=%s" %(form.openid.data, str(form.remember_me.data)))
		return redirect('/index')
	return render_template('login.html',title='Sign in',form=form, providers=app.config['OPENID_PROVIDERS'])