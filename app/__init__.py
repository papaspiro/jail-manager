from flask import render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bootstrap import Bootstrap
from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.mail import Mail
from flask.ext.admin import Admin
from flask.ext.moment import Moment
from flask import send_from_directory
from config import config
import os

db = SQLAlchemy()
bootstrap = Bootstrap()
admin =  Admin(name="Nsawam Prison MIS",template_mode='bootstrap3') #app,name='Jail Manager',template_mode='bootstrap3'
moment = Moment()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    

    app.config['UPLOAD_FOLDER'] = 'uploads'
    config[config_name].init_app(app)
    bootstrap.init_app(app)
    db.init_app(app)
    moment.init_app(app)
    admin.init_app(app)


    #routes and custom error pagesxx`
    #import blueprint modules
    from app.mod_auth.views import mod_auth as auth_blueprint
    from app.inmates import inmate_blueprint as inmatebp
    from inmates.models import Inmate


    @app.route('/pic/<path:filename>')
    def send_pic(filename):
        return send_from_directory('/images',filename) 


    @app.route('/uploads/<filename>')
    def uploaded_file(filename):
        return send_from_directory(app.config['UPLOAD_FOLDER'],filename)


    @app.route('/<path:path>')
    def static_image(path):
        return app.send_static_file(path)


    @app.errorhandler(404)
    def not_found(errorhandler):
        return render_template('404.html'),404

    @app.errorhandler(500)
    def internal_server_error(e):
        db.session.rollback()



    @app.route('/mypic/<path:filename>')
    def serve_static(filename):
        root_dir = os.path.dirname(os.getcwd())
        return send_from_directory(os.path.join(root_dir, 'static'), filename)


    app.register_blueprint(auth_blueprint)
    app.register_blueprint(inmatebp)


    #to be moved to where the app is run ???
    #courtesy of miguel @ flask tutorial
    #adding loggin functionality at app level
    if not app.debug:

        import logging
        from logging.handlers import RotatingFileHandler
        file_handler = RotatingFileHandler('logs/jailer.log', 'a', 1 * 1024 * 1024, 10)
        file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        app.logger.setLevel(logging.INFO)
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
        app.logger.info('jailermanager startup')

    return app





