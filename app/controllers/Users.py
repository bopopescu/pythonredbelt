
from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)

        self.load_model('User')
        self.load_model('Travel')

    def index(self):

        return self.load_view('/users/index.html')

    def new(self):
        new_user_info = {
        "name" : request.form['name'],
        "username" : request.form['username'],
        "password" : request.form['password'],
        "confirm_pw" : request.form['confirm_pw']
        }
        validate = self.models['User'].validate_new_user(new_user_info)
        if validate['status']:
            newuser = self.models['User'].create_new_user(new_user_info)
            print "newuser", newuser
            newid = self.models['User'].get_newest_user()
            session['id'] = newid['id']
            print "session id:", session['id']
            return redirect('/travels')
        else:
            flash(validate['errors'])
            return redirect('/')

    def login(self):
        login_info = {
        "username" : request.form['username'],
        "password" : request.form['password']
        }
        validation = self.models['User'].login_verification(login_info)
        if validation['status']:
            login_info = self.models['User'].login_user(login_info)
            session['id'] = login_info[0]['id']
            print "session id ==", session['id']
            return redirect('/travels')
        else:
            flash (validation['errors'])
            return redirect('/')

    def logout(self):
        session.clear()
        return redirect('/')
