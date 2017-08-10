from flask import Blueprint, request, jsonify, url_for
from mod_memory.models import Memory
from mod_auth.models import User

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
    user_to_add = 'deelaws89@gmail.com'
    user = User.query.filter_by(email=user_to_add).first()
    print(user.email)
    user.memories.append(new_memory)
    db.session.add(new_memory)
    db.session.commit()

    return jsonify(status = "200", 
                    location = url_for('memory.get_memory', id=new_memory.id, _external=True))
    # return jsonify(new_memory.to_json()), 201, \
    #     {'Location': url_for('memory.get_memory', id=new_memory.id, _external=True)}

@mod_memory.route('/edit', methods=['POST'])
def edit_memory():
    print("************ EDIT - MEMORY **************")
    print(request.json)
    print("*****************************************")
    