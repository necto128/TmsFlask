from typing import Union

from flask import render_template, request, redirect, url_for
from services.idea_service import IdeaServices

from models.models import User, Idea, db
from schemas.schemas import UserSchema


def show_users():
    return render_template("users.html", users=User.query.all())


def create_user() -> Union[redirect, render_template]:
    if request.method == "POST":
        user = UserSchema().load(request.form)
        db.session.add(User(username=user['username'], password=user['password']))
        db.session.commit()
        return redirect(url_for("app_urls.show_users"))
    else:
        return render_template("create_user.html")


def show_user(user_id: int) -> render_template:
    return render_template(
        "show_user.html",
        ideas=Idea.query.filter_by(user_id=user_id).all(),
        user=User.query.get(user_id))


def create_idea(user_id: int) -> redirect:
    IdeaServices.save_idea(user_id)
    return redirect(url_for("app_urls.show_user", user_id=user_id))
