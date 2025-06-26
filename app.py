from flask import Flask
from config import Config
from extensions import db
from models.episode import Episode
from models.guest import Guest
from models.appearance import Appearance

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

# Optional: if you want db.create_all() on launch
# with app.app_context():
#     db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
