from flask import render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bootstrap import Bootstrap
from flask import Flask

from flask.ext.admin import Admin
#from flask

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
admin =  Admin(app,name='Jail Manager',template_mode='bootstrap3')


#supperadmin


#flask admin
#admin = Admin(app, name='Jailer', template_mode='bootstrap3')

@app.errorhandler(404)
def not_found(errorhandler):
	return render_template('404.html'),404

@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'),500

#import blueprint modules
from app.mod_auth.views import mod_auth as auth_blueprint
from app.inmates.views import inmate_blueprint as inmatebp
from inmates.models import Inmate


app.register_blueprint(auth_blueprint)
app.register_blueprint(inmatebp)



