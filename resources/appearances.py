from flask_restful import Resource, reqparse
from models.appearance import Appearance
from models.episode import Episode
from models.guest import Guest
from extensions import db

class AppearanceCreateResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("rating", type=int, required=True, help="Rating is required")
        parser.add_argument("episode_id", type=int, required=True)
        parser.add_argument("guest_id", type=int, required=True)
        args = parser.parse_args()

        rating = args["rating"]
        episode_id = args["episode_id"]
        guest_id = args["guest_id"]

        errors = []

        if rating < 1 or rating > 5:
            errors.append("Rating must be between 1 and 5")

        episode = Episode.query.get(episode_id)
        if not episode:
            errors.append("Episode not found")

        guest = Guest.query.get(guest_id)
        if not guest:
            errors.append("Guest not found")

        if errors:
            return {"errors": errors}, 400

        appearance = Appearance(
            rating=rating,
            episode_id=episode_id,
            guest_id=guest_id
        )

        db.session.add(appearance)
        db.session.commit()

        response = appearance.to_dict()
        response["episode"] = episode.to_dict(only=("id", "date", "number"))
        response["guest"] = guest.to_dict(only=("id", "name", "occupation"))

        return response, 201
