from flask import Flask
from flask import render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

@app.errorhandler(404)
def not_found():
	return render_template('404'.html)


#import blueprint modules
from app.mod_auth.views import mod_auth as auth_blueprint

#register blueprints
app.register_blueprint(auth_blueprint)

