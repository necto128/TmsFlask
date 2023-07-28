import os

import requests
from dotenv import load_dotenv

from schemas.schemas import IdeaSchema

load_dotenv()


def generate_idea() -> dict:
    try:
        response = requests.get(os.environ.get('URL_IDEA'))
    except Exception:
        return {"Error": "Source is not exist"}
    data = IdeaSchema().load(response.json())
    return data
