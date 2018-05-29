import os

from flask import Flask
from werkzeug.contrib.fixers import ProxyFix
from flask_pymongo import PyMongo
from flask_login import LoginManager

def create_app():


	# common prefix for all routes in blueprints
	APP_URL_PREFIX = os.environ.get('MY_APP_PREFIX',None)

	# common prefix will also be prefix for static files
	APP_STATIC_URL = '/static'
	if APP_URL_PREFIX:
		APP_STATIC_URL = APP_URL_PREFIX + APP_STATIC_URL 
	
	app = Flask(__name__,static_url_path=APP_STATIC_URL)
	# important: use the following to respect X-Forwarded-Proto when https!
	app.wsgi_app = ProxyFix(app.wsgi_app)
			
	# app prefix will be used also for open redirect attempts detection
	app.config['REDIRECT_PREFIX'] = APP_URL_PREFIX+'/'
	
	# secret key of application
	app.config['SECRET_KEY'] = os.environ['MY_APP_SECRET_KEY']
	
		
	# mongodb database name
	app.config['MONGO_DBNAME'] = os.environ.get('MY_APP_MONGODB_NAME',app.name)
	# configure mongo
	mongo.init_app(app)
	
	
	# register all blueprints
	from .views import blueprints
	for bp in blueprints:
		app.register_blueprint(bp,url_prefix=APP_URL_PREFIX)


	# configure login_manager
	login_manager.init_app(app)
	login_manager.login_view = 'login.login_page'	

		
	return app

	
mongo = PyMongo()
login_manager = LoginManager() 
app = create_app()	
	
