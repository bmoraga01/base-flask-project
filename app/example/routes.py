from flask import Blueprint
from flask_restful import Api
from .views import *

bands_bp = Blueprint('bands', __name__, url_prefix='/api')
api = Api(bands_bp)

api.add_resource(BandListApiView, '/bands')
api.add_resource(BandDetailApiView, '/bands/<int:id>')