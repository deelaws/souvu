from flask import Blueprint
from mod_memory.models import Memory

from app.app import db

mod_memory = Blueprint('memory', __name__, url_prefix='/mem')


@mod_memory.route('/hello', methods=['GET'])
def mod_memory_hello():
    return "hello from mod memory"

@mod_memory.route('/getmem/<int:id>', methods=['GET'])
def get_memory():
    return "not_impl"

@mod_memory.route('/create', methods=['GET', 'POST'])
def create_memory():
    print("*****************************************")
    print(request.json)
    print("*****************************************")
    new_memory = Memory.from_json(request.json)

    # TODO: new_memory.user = g.current_user
    user_to_add = 'walter@example.com'
    user = User.query.filter_by(email=user_to_add).first()
    user.memories.append(new_memory)
    db.session.add(new_memory)
    db.session.commit()

    return jsonify(new_memory.to_json()), 201, \
        {'Location': url_for('memory.get_memory', id=new_memory.id, _external=True)}
