from flask_sqlalchemy import SQLAlchemy

from app.app import db
from app.models import Base
from mod_memory.memory_types import MemoryTypes

class Memory(Base):
    __tablename__ = 'memory'

    mem_name = db.Column(db.String(30), nullable=False)
    mem_info = db.Column(db.String(150), nullable=False)
    mem_type = db.Column(db.Enum(MemoryTypes), nullable=False)

    # Each Memory is associate with a USER.
    user_id = db.Column(db.Integer, db.ForeignKey('souvu_user.id'))
    user = db.relationship('User', backref="memories")

    def __init__(self, name, info, mtype):
        self.mem_name = name
        self.mem_info = info
        self.mem_type = mtype