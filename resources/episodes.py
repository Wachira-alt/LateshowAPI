from flask_restful import Resource
from models.episode import Episode
from extensions import db
from flask import abort
from models.appearance import Appearance

class EpisodeListResource(Resource):
    def get(self):
        episodes = Episode.query.all()
        return [ep.to_dict(only=("id", "date", "number")) for ep in episodes], 200
class EpisodeDetailResource(Resource):
    def get(self, id):
        episode = Episode.query.get(id)
        if not episode:
            return {"error": "Episode not found"}, 404

        ep_data = episode.to_dict()
        ep_data["appearances"] = [
            ap.to_dict(include=("id", "rating", "guest_id", "episode_id", "guest"))
            for ap in episode.appearances
        ]

        return ep_data, 200
