from flask import Blueprint

from views.view_main import (
    show_users, create_user, show_user, create_idea
)

app_urls = Blueprint('app_urls', __name__)

app_urls.add_url_rule('/users', view_func=show_users, methods=["GET"])
app_urls.add_url_rule('/create_user', view_func=create_user, methods=["GET", "POST"])
app_urls.add_url_rule('/user/<int:user_id>', view_func=show_user, methods=["GET"])
app_urls.add_url_rule('/user/<int:user_id>/create_idea', view_func=create_idea, methods=["GET"])
