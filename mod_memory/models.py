from flask_sqlalchemy import SQLAlchemy

from app.app import db
from app.models import Base

class Memory(Base):
    __tablename__ = 'memory'

    memory_name = db.Column(db.String(30), nullable=False)
    memory_info = db.Column(db.String(150), nullable=False)
