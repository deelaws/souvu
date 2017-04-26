
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"


if __name__ == "__main__":
    db.init_app(app)

    from souvu.mod_memory.views import mod_memory

    app.register_blueprint(mod_memory)
    app.run()
