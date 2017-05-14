
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

foo = "hello"
db = SQLAlchemy()

'''
    @app.route("/")
    def hello():
        return "Hello World"
'''

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:12345qaz@localhost/souvu'
    db.init_app(app)
    from mod_memory.views import mod_memory
    app.register_blueprint(mod_memory)

    print(app.url_map)
    
    return app