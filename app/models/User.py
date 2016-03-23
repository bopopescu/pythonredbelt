
from system.core.model import Model
from flask import session
import re

class User(Model):
    def __init__(self):
        super(User, self).__init__()

    def get_all_users(self):
        print self.db.query_db("SELECT * FROM users")

    def get_current_user(self):
        user_id = session['id']
        get_query = "SELECT * FROM users WHERE users.id = %s"
        get_info = [user_id]
        return self.db.query_db(get_query, get_info)

    def validate_new_user(self, info):
        errors = []
        password = info['password']
        if not info['name']:
            errors.append('Name cannot be blank')
        elif len(info['name']) < 2:
            errors.append('Name must be at least 2 characters long')
        if not info['username']:
            errors.append('username cannot be blank')
        if not info['password']:
            errors.append('Password cannot be blank')
        elif len(info['password']) < 8:
            errors.append('Password must be at least 8 characters long')
        elif info['password'] != info['confirm_pw']:
            errors.append('Password and confirmation must match!')
        if errors:
            return {"status": False, "errors": errors}
        else:
            return{"status": True}

    def create_new_user(self, info):
        pw_hash = self.bcrypt.generate_password_hash(info['password'])
        print "creating new user"
        new_user_query = "INSERT INTO users (name, username, pw_hash) VALUES (%s, %s, %s)"
        new_user_data = [info['name'], info['username'], pw_hash]
        return self.db.query_db(new_user_query, new_user_data)

    def get_newest_user(self):
        query = "SELECT id FROM users ORDER BY id DESC LIMIT 1"
        return self.db.query_db(query)[0]

    def login_user(self, info):
        try:
            login_query = "SELECT * FROM users WHERE username = %s"
            login_info = [info['username']]
            return self.db.query_db(login_query, login_info)
        except:
            return redirect('/')

    def login_verification(self, info):
        username = info['username']
        errors = []
        try:
            verify_hash_query = "SELECT id, username, pw_hash FROM users WHERE username = %s"
            verify_hash_data = [username]
            query_return = self.db.query_db(verify_hash_query, verify_hash_data)
            password = info['password']
            print query_return, "QUERY RETURN"
            if username == query_return[0]['username']:
                print "username match"
                if self.bcrypt.check_password_hash(query_return[0]['pw_hash'], password):
                    print "passed pw validation"
                    return {"status" : True}
                else:
                    print "failed pw validation"
                    errors.append('incorrect password.')
                    return {"status": False, "errors" : errors}
        except:
            print "bad username."
            errors.append('bad username.')
            return {"status": False, "errors": errors}

    def get_single_user(self, info):
        newinfo = info[0]['user_id']
        get_query = "SELECT * FROM users WHERE users.id = %s"
        get_info = [newinfo]
        return self.db.query_db(get_query, get_info)
