from flask import Blueprint
from flask_restful import Api
from .episodes import EpisodeListResource, EpisodeDetailResource
from .guests import GuestListResource
from .appearances import AppearanceCreateResource


# Create blueprint and API object
api_bp = Blueprint("api", __name__)
api = Api(api_bp)

# Episode routes

api.add_resource(EpisodeListResource, "/episodes")
api.add_resource(EpisodeDetailResource, "/episodes/<int:id>")

#Guests
api.add_resource(GuestListResource, "/guests")

#appearance
api.add_resource(AppearanceCreateResource, "/appearances")



