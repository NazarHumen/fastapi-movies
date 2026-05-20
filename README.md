# Movies API (FastAPI)

REST API for a catalog of movies and directors. Built on FastAPI +
SQLAlchemy + PostgreSQL. Full CRUD for movies, creation of directors,
genre filtering, and listing all movies for a given director.

## Features

- CRUD for movies (`/movies`) — create, read, update, delete
- Create and list directors (`/directors`)
- Movies by director via `/directors/{id}/movies`
- Genre filtering: `GET /movies?genre=Sci-Fi`
- Pagination via `skip` / `limit`
- Pydantic validation: `rating` is constrained to `0 ≤ rating ≤ 10`
  (422 on violation)
- Nested serializer: the movie response includes the director object
  (`director_rel`)
- Auto-generated OpenAPI docs at `/docs` and `/redoc`
- Config via `.env` (`pydantic-settings`), PostgreSQL as the database

## Tech Stack

- Python 3.11+
- FastAPI 0.136
- SQLAlchemy 2.0
- Pydantic 2 + pydantic-settings
- PostgreSQL (psycopg2-binary)
- Uvicorn

## Installation

```bash
git clone https://github.com/example.git
cd movie_api

python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # Linux / macOS

pip install -r requirements.txt

cp .env.example .env
# fill in DATABASE_URL for your database

uvicorn main:app --reload
```

After startup:

- API: http://127.0.0.1:8000
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

Tables are created automatically on app startup
(`models.Base.metadata.create_all`).

## Project Structure

```
main.py          FastAPI entry point, /directors and /movies routes
models.py        SQLAlchemy models: Director and Movie
schemas.py       Pydantic schemas (Create / Response)
crud.py          DB operations (get / create / update / delete)
database.py      engine, SessionLocal, get_db() dependency
config.py        Settings via pydantic-settings (reads .env)
screenshots/     screenshots of an API test run
```

## Environment Variables

Configured via `.env` (not committed). See `.env.example` for the
template.

| Variable | Description |
|---|---|
| `DATABASE_URL` | PostgreSQL connection URL, e.g. `postgresql://user:password@localhost:5432/movies` |

## Endpoints

### Directors

- `GET    /directors` — list directors (`skip`, `limit`)
- `POST   /directors` — create a director (201)
- `GET    /directors/{id}/movies` — movies of a specific director

### Movies

- `GET    /movies` — list movies (`skip`, `limit`, `genre`)
- `GET    /movies/{id}` — get a movie by id (404 if missing)
- `POST   /movies` — create a movie (201)
- `PUT    /movies/{id}` — full update of a movie
- `DELETE /movies/{id}` — delete a movie

## Screenshots

Full pass through the API — one screenshot per case, in order.

| # | Test case | Preview |
|---|---|---|
| 1 | `POST /directors` — director created (201) | ![post director 201](screenshots/01_post_director_created.png) |
| 2 | `POST /movies` — movie created with nested director (201) | ![post movie 201](screenshots/02_post_movie_with_director.png) |
| 3 | `POST /movies` — `rating > 10` validation (422) | ![post movie 422](screenshots/03_post_movie_rating_validation.png) |
| 4 | `GET /movies?genre=Sci-Fi` — filter by genre | ![movies genre filter](screenshots/04_get_movies_genre_filter.png) |
| 5 | `GET /movies/1` — fetch movie by id | ![movie by id](screenshots/05_get_movie_by_id.png) |
| 6 | `GET /movies/999` — 404 handling | ![movie 404](screenshots/06_get_movie_not_found.png) |
| 7 | `PUT /movies/1` — rating update | ![movie put](screenshots/07_put_movie_updated.png) |
| 8 | `DELETE /movies/2` — movie deleted | ![movie delete](screenshots/08_delete_movie_success.png) |
| 9 | `GET /directors/1/movies` — director's movies | ![director movies](screenshots/09_get_director_movies.png) |

## Author

**Nazar Humen**
GitHub: [@NazarHumen](https://github.com/NazarHumen)
Email: nazargumen11@gmail.com
