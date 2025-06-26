from flask import Blueprint
from flask_restful import Api
from .episodes import EpisodeListResource, EpisodeDetailResource

# Create blueprint and API object
api_bp = Blueprint("api", __name__)
api = Api(api_bp)

# Episode routes

api.add_resource(EpisodeListResource, "/episodes")
api.add_resource(EpisodeDetailResource, "/episodes/<int:id>")

