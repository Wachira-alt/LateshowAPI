from extensions import db
from sqlalchemy_serializer import SerializerMixin

class Episode(db.Model, SerializerMixin):
    __tablename__ = 'episodes'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String, nullable=False)
    number = db.Column(db.Integer, nullable=False)

    appearances = db.relationship(
        'Appearance',
        backref='episode',
        cascade='all, delete-orphan'
    )

    serialize_rules = ('-appearances.episode',)
