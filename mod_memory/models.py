from flask_sqlalchemy import SQLAlchemy
from flask import url_for

from app.app import db
from app.models import Base
from mod_memory.memory_types import MemoryTypes

from collections import OrderedDict

class ValidationError(ValueError):
    pass

class DictSerializable(object):
    def _asdict(self):
        result = OrderedDict()
        for key in self.__mapper__.c.keys():
            result[key] = getattr(self, key)
        return result

class Memory(Base, DictSerializable):
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

    def to_json(self):
        memory_json = {
            'mem_name': self.mem_name,
            'mem_url': url_for('memory.get_memory', id=self.id, _external=True),
            'mem_info': self.mem_info,
            'mem_type': self.mem_type,
        }

        return memory_json

    @staticmethod
    def from_json(mem_json):
        mname = mem_json.get('mem_name')
        minfo = mem_json.get('mem_info')
        mtype = mem_json.get('mem_type')

        if mname is None or mname == '':
            raise ValidationError('Memory does not have a name')
        if minfo is None or minfo == '':
            raise ValidationError('Memory does not have an info')

        mtype = MemoryTypes.get_type_from_string(mtype)
        if mtype is None or mtype == '':
            raise ValidationError('Memory does not have a type')

        return Memory(mname, minfo, mtype)

