from flask import Blueprint
from mod_memory.models import Memory

mod_memory = Blueprint('memory', __name__, url_prefix='/mem')


@mod_memory.route('hello', methods=['GET'])
def mod_memory_hello():
    return "hello from mod memory"
