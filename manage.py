import os
from app.inmates.models import *
from app  import  create_app,db
from flask.ext.script import Manager,Shell
from flask.ext.migrate import Migrate,MigrateCommand

app = create_app(os.getenv('INSIGHT_CONFIG') or 'default' )
#app.config[]
#app.config.from_object('config')

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  #response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept,Authorization')

  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
  response.headers.add('Accept', 'application/json')
  return response



manager = Manager(app)
migrate = Migrate(app, db)




def make_shell_context():
	return dict(app=app,db=db)


manager.add_command('shell',Shell(make_context=make_shell_context))
manager.add_command('db',MigrateCommand)


if __name__ == '__main__':
	manager.run()
