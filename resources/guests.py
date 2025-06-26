from flask_restful import Resource
from models.guest import Guest

class GuestListResource(Resource):
    def get(self):
        guests = Guest.query.all()
        return [guest.to_dict(only=("id", "name", "occupation")) for guest in guests], 200
