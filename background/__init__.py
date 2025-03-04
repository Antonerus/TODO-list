import os

from flask import Flask

def create_app(test_config=None):
	#create the app and setup its configurations
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_mapping(
		SECRET_KEY='dev', 
		DATABASE=os.path.join(app.instance_path, 'background.sqlite'),
	)
	
	if test_config is None:
		app.config.from_pyfile('config.py', silent=True)
	else:
		app.config.from_mapping(test_config)

	try:
		os.makedirs(app.instance_path)
	except OSError:
		pass
		
	@app.route('/hello')
	def hello():
		return 'Hello World!'
	#register database
	from . import db
	db.init_app(app)

	from . import home
	app.register_blueprint(home.bp)
	app.add_url_rule('/', endpoint='index')	
	
	return app
