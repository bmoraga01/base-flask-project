from flask import Flask, jsonify
from flask_restful import Api

from .db import db
from .ext import marshmallow, migrate, cors
from .common.error_handling import AppErrorBaseClass, ObjectNotFound

from .example.routes import bands_bp

def create_app(settings_module):
    app = Flask(__name__)
    app.config.from_object(settings_module)
    
    # Inicializa las extenciones
    db.init_app(app)
    marshmallow.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app, resources={
        r'/api/*': { 'origins': ['http://localhost:3000'] }
    })
    
    # Captura todos los errores
    Api(app, catch_all_404s=True)
    register_error_handlers(app)
    
    # Registra los blueprints
    app.register_blueprint(bands_bp)
    
    return app

def register_error_handlers(app: Flask):
    @app.errorhandler(Exception)
    def handle_exception_error(e):
        return jsonify({ 'msg': 'Internal Server Error' }), 500
    
    @app.errorhandler(405)
    def handler_405_error(e):
        return jsonify({ 'msg': 'Method not Allowed' }), 405
    
    @app.errorhandler(404)
    def handler_404_error(e):
        return jsonify({ 'msg': 'Not Found Error' }), 404
    
    @app.errorhandler(403)
    def handler_403_error(e):
        return jsonify({ 'msg': 'Forbidden Error' }), 403
    
    @app.errorhandler(AppErrorBaseClass)
    def handle_app_base_error(e):
        return jsonify({ 'msg': str(e) }), 500
    
    @app.errorhandler(ObjectNotFound)
    def handle_object_not_found_error(e):
        return jsonify({ 'msg': str(e) }), 404