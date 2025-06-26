
# Late Show API

This is a Flask RESTful API for managing episodes, guests, and their appearances on the Late Show. The app uses SQLAlchemy with Flask-Migrate and follows a modular structure for clean, scalable development.

---

## Project Structure

```

├── app.py
├── config.py
├── extensions.py
├── seed.py
├── .env
├── .env.example
├── models/
│   ├── **init**.py
│   ├── episode.py
│   ├── guest.py
│   └── appearance.py
├── resources/
│   ├── **init**.py
│   ├── episodes.py
│   ├── guests.py
│   └── appearances.py

````

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/wachira-alt/lateshowAPI.git
cd lateshowAPI
````

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

Use the provided `.env.example` as a template:

```
DATABASE_URL=sqlite:///app.db
```

---

## Database Setup

### 1. Run migrations

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 2. Seed the database

```bash
python seed.py
```

This will populate the database using the provided CSV guest data.

---

## Available Endpoints

All routes are prefixed with `/api`

### `GET /episodes`

Returns a list of all episodes.

```json
[
  {
    "id": 1,
    "date": "1/11/99",
    "number": 1
  }
]
```

---

### `GET /episodes/<id>`

Returns an episode and its guest appearances.

```json
{
  "id": 1,
  "date": "1/11/99",
  "number": 1,
  "appearances": [
    {
      "id": 1,
      "rating": 4,
      "guest_id": 1,
      "episode_id": 1,
      "guest": {
        "id": 1,
        "name": "Michael J. Fox",
        "occupation": "actor"
      }
    }
  ]
}
```

If the episode is not found:

```json
{ "error": "Episode not found" }
```

---

### `GET /guests`

Returns a list of all guests.

```json
[
  {
    "id": 2,
    "name": "Sandra Bernhard",
    "occupation": "Comedian"
  }
]
```

---

### `POST /appearances`

Creates a new guest appearance on an episode.

**Request Body:**

```json
{
  "rating": 5,
  "episode_id": 2,
  "guest_id": 3
}
```

**Success Response:**

```json
{
  "id": 162,
  "rating": 5,
  "guest_id": 3,
  "episode_id": 2,
  "episode": {
    "id": 2,
    "date": "1/12/99",
    "number": 2
  },
  "guest": {
    "id": 3,
    "name": "Tracey Ullman",
    "occupation": "television actress"
  }
}
```

**Error Response:**

```json
{
  "errors": [
    "Rating must be between 1 and 5",
    "Guest not found"
  ]
}
```

---

## Running the Server

```bash
flask run
```

The app will run on `http://localhost:5000/api`

---

## Author
Dennis Wachira
[GitHub: wachira-alt](https://github.com/Wachira-alt/LateshowAPI)


