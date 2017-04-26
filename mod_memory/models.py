from flask_sqlalchemy import SQLAlchemy
from souvu.app import db
from souvu.models import Base


class Memory(Base):
    __tablename__ = 'memory'

    memory_name = db.Column(db.String(30), nullable=False)
    memory_info = db.Column(db.String(150), nullable=False)
