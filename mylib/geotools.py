"""Build a library of geo tools"""


from geopy import distance, geocoders


def get_cities():
    """Return a list of 10 most populous cities in the US"""
    cities = [
        "New York, NY",
        "Los Angeles, CA",
        "Chicago, IL",
        "Houston, TX",
        "Piladelphia, PA",
        "Phoenix, AZ",
        "San Antonio, TX",
        "San Diego, CA",
        "Dallas, TX",
        "San Jose, CA",
    ]
    return cities


def get_distance(city1, city2):
    """Get distance between two cities"""
    geolocator = geocoders.Nominatim(user_agent="python-testing-app")
    loc1 = geolocator.geocode(city1)
    loc2 = geolocator.geocode(city2)
    return distance.distance(loc1.point, loc2.point).miles
