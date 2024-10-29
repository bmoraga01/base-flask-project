from flask import request
from flask_restful import Resource

from ..common.generate_response import generate_response
from ..common.http_code import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND

from .models import Band, Member

class BandListApiView(Resource):
    
    def get(self):
        data = Band.get_all()
        response = []
        return generate_response(data=response, message='Bands List', status=HTTP_200_OK)
    
    def post(self):
        data = request.get_json()
        
        return generate_response()
    
class BandDetailApiView(Resource):
    
    def get(self, id):
        pass
    
    def put(self, id):
        pass
    
    def delete(self, id):
        pass
    
class MemberListApiView(Resource):
    
    def get(self):
        pass
    
    def post(self):
        pass
    
class MemberDetailApiView(Resource):
    
    def get(self, id):
        pass
    
    def put(self, id):
        pass
    def delete(self, id):
        pass