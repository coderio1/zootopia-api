"""
Fetching animal data from the API Ninjas service.
Returns list of dictionaries.
"""

import os
import requests
from dotenv import load_dotenv

# Load variables from .env into the environment
load_dotenv()

API_KEY = os.getenv('API_KEY')
API_URL = 'https://api.api-ninjas.com/v1/animals'


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    """
    if not API_KEY:
        raise RuntimeError(
            "API_KEY is not set. Make sure you have a .env file with API_KEY=..."
        )

    response = requests.get(
        API_URL,
        headers={'X-Api-Key': API_KEY},
        params={'name': animal_name},
        timeout=10
    )
    response.raise_for_status()  # raises on 4xx / 5xx
    return response.json()
