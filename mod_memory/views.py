from flask import Blueprint

mod_memory = Blueprint('memory', __name__, url_prefix='/mem')


@mod_memory.route('hello', method=['GET'])
def mod_memory_hello():
    return "hello from mod memory"
