from flask import Blueprint

textmp_blueprint = Blueprint('textmp', __name__)


from . import views