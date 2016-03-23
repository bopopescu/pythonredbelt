
from system.core.controller import *
import datetime

class Travels(Controller):
    def __init__(self, action):
        super(Travels, self).__init__(action)

        self.load_model('Travel')
        self.load_model('User')

    def index(self):
        username = self.models['User'].get_current_user()
        othertravels = self.models['Travel'].get_notmy_travels()
        print othertravels, "THIS SHOULD BE THE ONES I AM NOT A PART OF"
        mytravels = self.models['Travel'].get_my_travels()
        print username, othertravels, mytravels
        return self.load_view('/travels/travelindex.html', user=username, mine=mytravels, others=othertravels)

    def add_plan(self):

        return self.load_view('/travels/add.html')

    def new(self):
        print "new page"
        new_travel_info = {
        "destination" : request.form['destination'],
        "plan" : request.form['plan'],
        "depart" : request.form['depart'],
        "returndate" : request.form['returndate'],
        "created_by" : session['id']
        }
        print new_travel_info
        if request.form['returndate'] > request.form['depart']:
            newplan = self.models['Travel'].new_travel_plan(new_travel_info)
            print "newplan", newplan
            return redirect('/travels')
        else:
            flash('return date must be after departure date.')
            return redirect('/travels/add')

    def destination(self, id):
        place = id
        place_info = self.models['Travel'].get_destination_by_id(place)
        tagalong_id = self.models['Travel'].get_tagalongs(place)
        print tagalong_id
        return self.load_view('travels/destination.html', info=place_info, tagalong=tagalong_id)


    def join(self, id):
        destination = id
        destination_return = self.models['Travel'].add_user_to_trip(destination)
        print destination_return, "PRINTING DESTINATION RETURN"
        return redirect('/travels')
