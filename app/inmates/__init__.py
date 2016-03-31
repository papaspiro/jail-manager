from flask import Blueprint

inmate_blueprint = Blueprint('inmates',__name__,url_prefix='/inmates')

from . import views, errors
