from pydantic import BaseModel, Field


class DirectorBase(BaseModel):
    name: str
    country: str


class DirectorCreate(DirectorBase):
    pass


class DirectorResponse(DirectorBase):
    id: int

    class Config:
        from_attributes = True


class MovieBase(BaseModel):
    title: str
    year: int
    genre: str
    rating: float = Field(ge=0, le=10.0)


class MovieCreate(MovieBase):
    director_id: int


class MovieResponse(MovieBase):
    id: int
    director_id: int
    director_rel : DirectorResponse

    class Config:
        from_attributes = True
