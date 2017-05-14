from app.app import db, create_app, foo


print(foo)

app = create_app()

with app.app_context():
    db.create_all()


