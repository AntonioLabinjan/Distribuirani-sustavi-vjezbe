from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from app.models.movie import Movie
from app.models.actor import Actor
from app.models.writer import Writer
import json

router = APIRouter(prefix="/filmovi", tags=["Filmovi"])

movies: List[Movie] = []

def clean_movie_data(item: dict) -> dict:
    if "Runtime" in item and isinstance(item["Runtime"], str):
        try:
            runtime = int(item["Runtime"].split()[0])
            item["Runtime"] = runtime if runtime > 0 else 1
        except ValueError:
            item["Runtime"] = 1 

    if "imdbVotes" in item and isinstance(item["imdbVotes"], str):
        try:
            votes = int(item["imdbVotes"].replace(",", "").replace(".", "").strip())
            item["imdbVotes"] = votes if votes > 0 else 1
        except ValueError:
            item["imdbVotes"] = 1 

    if "imdbRating" in item:
        try:
            rating = float(item["imdbRating"])
            item["imdbRating"] = rating
        except (ValueError, TypeError):
            item["imdbRating"] = 0.0 

    if "Year" in item and isinstance(item["Year"], str):
        try:
            item["Year"] = int(item["Year"].split("–")[0])
        except ValueError:
            item["Year"] = 1900  

    if "Actors" in item and isinstance(item["Actors"], str):
        actors = []
        for a in item["Actors"].split(","):
            parts = a.strip().split(" ", 1)
            name = parts[0]
            surname = parts[1] if len(parts) > 1 else None
            actors.append(Actor(name=name, surname=surname))
        item["Actors"] = actors

    if "Writer" in item and isinstance(item["Writer"], str):
        writers = []
        for w in item["Writer"].split(","):
            parts = w.strip().split(" ", 1)
            name = parts[0]
            surname = parts[1] if len(parts) > 1 else None
            writers.append(Writer(name=name, surname=surname))
        item["Writer"] = writers

    return item



with open("app/data/movies.json", encoding="utf-8") as f:
    data = json.load(f)
    for item in data:
        clean_item = clean_movie_data(item)
        movies.append(Movie(**clean_item))


@router.get("/", response_model=List[Movie])
def get_all_movies(
    min_year: Optional[int] = Query(None, gt=1900),
    max_year: Optional[int] = None,
    min_rating: Optional[float] = Query(None, ge=0, le=10),
    max_rating: Optional[float] = Query(None, ge=0, le=10),
    type: Optional[str] = Query(None, pattern="^(movie|series)$"),
):
    result = movies

    if min_year is not None:
        result = [m for m in result if m.Year >= min_year]
    if max_year is not None:
        result = [m for m in result if m.Year <= max_year]
    if min_rating is not None:
        result = [m for m in result if m.imdbRating >= min_rating]
    if max_rating is not None:
        result = [m for m in result if m.imdbRating <= max_rating]
    if type is not None:
        result = [m for m in result if m.type == type]

    return result


@router.get("/imdb/{imdb_id}", response_model=Movie)
def get_movie_by_imdb_id(imdb_id: str):
    for movie in movies:
        if movie.imdbID == imdb_id:
            return movie
    raise HTTPException(status_code=404, detail="Movie not found")


@router.get("/title/{title}", response_model=Movie)
def get_movie_by_title(title: str):
    for movie in movies:
        if movie.Title.lower() == title.lower():
            return movie
    raise HTTPException(status_code=404, detail="Movie not found")
