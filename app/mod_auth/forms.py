from flask.ext.wtf import Form #RecaptchaField
from wtforms import StringField,BooleanField,PasswordField,TextField
from wtforms.validators import DataRequired, Required,Email,EqualTo


class LoginForm(Form):
	#openid = StringField('openid',validators=[ DataRequired() ])
	#remember_me = BooleanField("remember_me")
	email = TextField("Email Address",[Email(),Required(message="Please enter email address")])
	password = PasswordField("Password" ,[PasswordField(message="You must provide a password")])



