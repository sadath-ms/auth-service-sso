from flask import Blueprint
from app.views.user_view import UserAPI

user_routes = Blueprint("user", __name__)

# Route -> Class-based View
user_routes.add_url_rule("/users", view_func=UserAPI.as_view("user_api"))
