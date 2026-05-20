from sqlalchemy import ForeignKey, Column, Integer, String, Float
from sqlalchemy.orm import relationship
from database import Base


class Director(Base):
    __tablename__ = 'directors'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    country = Column(String, nullable=False)
    movies = relationship('Movie', back_populates='director_rel')


class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, index=True)
    year = Column(Integer, nullable=False)
    genre = Column(String, nullable=False)
    rating = Column(Float, nullable=False)
    director_id = Column(Integer, ForeignKey('directors.id'), nullable=False)
    director_rel = relationship('Director', back_populates='movies')
