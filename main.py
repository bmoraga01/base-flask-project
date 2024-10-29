from app import create_app
from dotenv import load_dotenv
from os import getenv

load_dotenv()

if getenv('FLASK_DEBUG', default=False):
    setting_module = 'config.DevConfig'
else:
    setting_module = 'config.ProdConfig'
    
app = create_app(setting_module)