import os 
basedir = os.path.abspath(os.path.dirname(__file__))

'''
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir ,'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')



WTF_CSRF_ENABLED = True
SECRET_KEY = 'who-jah-bless'

UPLOAD_FOLDER = 'app/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
'''

class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'its all about cryptosecr33t5'
	SQLALCHEMY_COMMIT_ON_TEAR_DOWN = True
	MAIL_SUBJECT_PREFIX  = ['Jailer Manager']
	MAIL_SENDER = 'Jailer Admin <admin@jailmanager.com>'
	JAILER_ADMIN = os.environ.get('JAILER_ADMIN')
	UPLOAD_FOLDER = 'app/uploads'
	ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])	

	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	DEBUG =True
	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
	MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') 
	SQLALCHEMY_DATABASE_URI =  'sqlite:///' + os.path.join(basedir, 'app.db')
	# os.environ.get('DEV_DATABASE_URL') or \
       # 'sqlite:///' + os.path.join(basedir, 'app.db')


class  TestingConfig(Config):
	TESTING = True
	SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
	'sqlite:///' + os.path.join(basedir, 'app.db')

class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')



config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}


