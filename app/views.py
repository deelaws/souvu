from flask import Blueprint, request, render_template, jsonify

from mod_memory.models import Memory

mod_app = Blueprint('app',__name__, url_prefix='/app')

@mod_app.route('/home', methods=['GET'])
def home():
    return "Hello World home"


@mod_app.route('/mems', methods=['GET', 'POST'])
def get_memories():
    print("Hello there I am here")
    print(request.json)
    my_mems = Memory.query.all()
    
    print(my_mems[0])
    if (not my_mems):
        return "{}"
    else:
        print("mooooooooooooooooooooooooooooooo")
        return jsonify(memories = [{'mem_name': my_mems[0].mem_name,
                                    'mem_info': my_mems[0].mem_info},
                                    {'mem_name': my_mems[0].mem_name,
                                    'mem_info': my_mems[0].mem_info}])