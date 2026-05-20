from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
import crud, models, schemas
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)
app = FastAPI(title="Movies API", version="1.0")


# Directors
@app.get('/directors', response_model=list[schemas.DirectorResponse], tags=["Directors"])
def list_directors(skip: int = 0, limit: int = 10,
                   db: Session = Depends(get_db)):
    return crud.get_directors(db, skip=skip, limit=limit)


@app.post('/directors', response_model=schemas.DirectorResponse,
          status_code=201, tags=["Directors"])
def create_director(director: schemas.DirectorCreate,
                    db: Session = Depends(get_db)):
    return crud.create_director(db, director)


@app.get('/directors/{director_id}/movies',
         response_model=list[schemas.MovieResponse], tags=["Directors"])
def get_director_movies(director_id: int, db: Session = Depends(get_db)):
    director = crud.get_director(db, director_id)
    if not director:
        raise HTTPException(status_code=404, detail="Director not found")
    return crud.get_director_movies(db, director_id)


# Movies
@app.get('/movies', response_model=list[schemas.MovieResponse], tags=["Movies"])
def list_movies(
        skip: int = 0,  # query param: ?skip=0
        limit: int = 10,  # query param: ?limit=10
        genre: str = None,  # query param: ?genre=Action
        db: Session = Depends(get_db)
):
    return crud.get_movies(db, skip=skip, limit=limit, genre=genre)


@app.get('/movies/{movie_id}', response_model=schemas.MovieResponse, tags=["Movies"])
def get_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = crud.get_movie(db, movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie


@app.post('/movies', response_model=schemas.MovieResponse, status_code=201, tags=["Movies"])
def create_movie(movie: schemas.MovieCreate, db: Session = Depends(get_db)):
    return crud.create_movie(db, movie)


@app.put('/movies/{movie_id}', response_model=schemas.MovieResponse, tags=["Movies"])
def update_movie(movie_id: int, movie: schemas.MovieCreate,
                 db: Session = Depends(get_db)):
    updated = crud.update_movie(db, movie_id, movie)
    if not updated:
        raise HTTPException(status_code=404, detail="Movie not found")
    return updated


@app.delete('/movies/{movie_id}', tags=["Movies"])
def delete_movie(movie_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_movie(db, movie_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Movie not found")
    return {"message": "Deleted successfully"}
