import csv
from extensions import db
from app import app
from models.episode import Episode
from models.guest import Guest
from models.appearance import Appearance

def clean_guest_names(raw_guest_list):
    return [name.strip() for name in raw_guest_list.split(',') if name.strip() != '']

def seed_database():
    with app.app_context():
        db.drop_all()
        db.create_all()

        with open('seed.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            episode_map = {}
            guest_map = {}

            for row in reader:
                raw_date = row['Show'].strip()
                occupation = row['GoogleKnowlege_Occupation'].strip()
                raw_guests = row['Raw_Guest_List'].strip()

                if raw_date == '' or raw_guests == '' or occupation == '':
                    continue  # Skip incomplete rows

                # 1. Create or retrieve the episode
                episode = episode_map.get(raw_date)
                if not episode:
                    episode = Episode(date=raw_date, number=len(episode_map) + 1)
                    db.session.add(episode)
                    db.session.flush()
                    episode_map[raw_date] = episode

                # 2. Create guests and appearances
                guest_names = clean_guest_names(raw_guests)
                for guest_name in guest_names:
                    guest = guest_map.get(guest_name)

                    if not guest:
                        guest = Guest(name=guest_name, occupation=occupation)
                        db.session.add(guest)
                        db.session.flush()
                        guest_map[guest_name] = guest

                    appearance = Appearance(
                        episode_id=episode.id,
                        guest_id=guest.id,
                        rating=5
                    )
                    db.session.add(appearance)

            db.session.commit()
            print(f"Seeded {len(episode_map)} episodes, {len(guest_map)} guests.")

if __name__ == '__main__':
    seed_database()
