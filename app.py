from fastapi import FastAPI
import uvicorn
from mylib.geotools import get_distance, get_cities
from mylib.wiki import get_wiki_keywords

app = FastAPI()


@app.get("/")
async def root():
    """Home page route for get method"""
    return {"message": "Hello World"}


@app.get("/distance/{city1}/{city2}")
async def get_distancex(city1: str, city2: str):
    """Get distance between two points"""
    return {"distance": get_distance(city1, city2)}


@app.get("/keywords/{keyword}")
async def get_keywords(keyword: str):
    """Get keywords from wiki page"""
    return {"keywords": get_wiki_keywords(keyword)}


@app.get("/cities")
async def get_citiesx():
    """Get list of cities"""
    return {"cities": get_cities()}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
