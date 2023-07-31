import os

import requests
from dotenv import load_dotenv

from models.models import Idea, db
from schemas.schemas import IdeaSchema

load_dotenv()


class IdeaServices:
    @staticmethod
    def generate_idea() -> dict:
        try:
            response = requests.get(os.environ.get('URL_IDEA'))
        except Exception:
            return {"Error": "Source is not exist"}
        data = IdeaSchema().load(response.json())
        return data

    @staticmethod
    def save_idea(user_id):
        idea = IdeaServices.generate_idea()
        db.session.add(Idea(
            type=idea['type'],
            activity=idea['activity'],
            accessibility=idea['accessibility'],
            price=idea['price'],
            user_id=user_id
        ))
        db.session.commit()
