
from system.core.model import Model
from flask import session

class Travel(Model):
    def __init__(self):
        super(Travel, self).__init__()

    def get_notmy_travels(self):
        user = session['id']
        travelquery =  "SELECT travels.id, travels.destination, travels.depart, travels.returndate, travels.plan, travels.created_by, tagalongs.user_id FROM travels LEFT JOIN tagalongs ON travels.id = tagalongs.trip_id WHERE travels.created_by != %s AND (tagalongs.user_id != %s OR tagalongs.user_id IS null)"
        traveldata = [user, user]
        return self.db.query_db(travelquery, traveldata)

    def get_my_travels(self):
        user = session['id']
        travelsquery = "SELECT travels.destination, travels.depart, travels.returndate, travels.plan, travels.created_by, tagalongs.user_id FROM travels LEFT JOIN tagalongs ON travels.id = tagalongs.trip_id WHERE tagalongs.user_id = %s OR travels.created_by = %s"
        travelsdata = [user, user]
        return self.db.query_db(travelsquery, travelsdata)

    def new_travel_plan(self, info):
        userid = session['id']
        print userid
        planquery = "INSERT INTO travels (destination, plan, depart, returndate, created_by) VALUES  (%s, %s, %s, %s, %s)"
        plandata = [info['destination'], info['plan'], info['depart'], info['returndate'], info['created_by']]
        return self.db.query_db(planquery, plandata)

    def get_destination_by_id(self, info):
        destinquery = "SELECT travels.id, travels.destination, travels.plan, travels.depart, travels.returndate, travels.created_by, users.name FROM travels JOIN users ON travels.created_by = users.id WHERE travels.id = %s"
        destindata = [info]
        return self.db.query_db(destinquery, destindata)

    def add_user_to_trip(self, info):
        current_user = session['id']
        addtotripquery = "INSERT INTO tagalongs (trip_id, user_id) VALUES (%s, %s)"
        addtotripdata = [info, current_user]
        return self.db.query_db(addtotripquery, addtotripdata)

    def get_tagalongs(self, info):
        tagalongQuery = "SELECT users.name FROM users JOIN tagalongs ON tagalongs.user_id = users.id WHERE tagalongs.trip_id = %s"
        print info, "THIS IS THE TAGALONG PASSSALONG"
        tagalongData = [info]
        return self.db.query_db(tagalongQuery, tagalongData)
