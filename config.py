from dotenv import load_dotenv
from os import getenv

class Config:
    """Establece la configuración de Flask desde el archivo .env"""
    
    # General Config
    SECRET_KEY              = getenv('SECRET_KEY')
    TESTING                 = getenv('TESTING', default=False)
    
    PROPAGATE_EXCEPTIONS    = getenv('PROPAGATE_EXCEPTIONS')
    ERROR_404_HELP          = getenv('ERROR_404_HELP')
    
    # Database
    SQLALCHEMY_TRACK_MODIFICATIONS  = getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
    SHOW_SQLALCHEMY_LOG_MESSAGES    = getenv('SHOW_SQLALCHEMY_LOG_MESSAGES')
    SQLALCHEMY_ECHO                 = getenv('SQLALCHEMY_ECHO')
    
class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI         = getenv('SQLALCHEMY_DATABASE_URI_LOCAL')

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI         = getenv('SQLALCHEMY_DATABASE_URI')