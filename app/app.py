
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

foo = "hello"
db = SQLAlchemy()
login_manager = LoginManager()

login_manager.login_message = 'Successful login'
login_manager.login_view = 'auth.login'
login_manager.login_message = 'Please log in #todo localization'

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:12345qaz@localhost/souvu'
    app.config["SECRET_KEY"] = "ITSASECRET"
    db.init_app(app)
    login_manager.init_app(app)

    # Register Blueprints
    from mod_memory.views import mod_memory
    from mod_auth.views import mod_auth
    app.register_blueprint(mod_memory)
    app.register_blueprint(mod_auth)

    @app.route("/")
    def hello():
        return "Hello World"

    print(app.url_map)
    
    return app