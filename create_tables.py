from app.app import db, create_app
from mod_auth.models import User
from mod_memory.models import Memory
from mod_memory.memory_types import MemoryTypes

from random import randint


def create_reminders():
    pass

app = create_app()

users_to_add = [('deelaws@hotmail.com', 'qwqwqwqwqw'),
                ('besttimothy1@gmail.com', 'qwqwqwqwqw'),
                ('jordanb@hotmail.com', 'qwqwqwqwqw'),
                ('deelaws89@gmail.com', 'qwqwqwqwqw')]

def create_sample_users():
    
    for user in users_to_add:
        print("Username: \'%s\', password: \'%s\'" % (user[0], user[1]))
        new_user = User(user[0], user[1])
        new_user.test_account = True
        db.session.add(new_user)

    db.session.commit()

def create_sample_vocabulary_memories(num):
    users = db.session.query(User).all()
    num_users = len(users_to_add)

    print("Number of users {}.".format(num_users))
    # Just add the same reminder for each User
    for i in range(0,num):
        # pick random user
        user_num = randint(0,num_users-1)

        mem_name = "Tumultuous"
        mem_info = "making a loud, confused noise; uproarious."
        new_mem = Memory(mem_name, mem_info, MemoryTypes.VOCABULARY)
        users[user_num].memories.append(new_mem)

    for u in users:
        db.session.add(u)

    db.session.commit()


def refresh_db():
    with app.app_context():
        db.drop_all()
        db.create_all()
        create_sample_users()
        create_sample_vocabulary_memories(10)

if __name__ == "__main__":
    refresh_db()