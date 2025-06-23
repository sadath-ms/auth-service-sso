from flask import Blueprint
from app.views.user_view import UserAPI
from app.views.auth_view import IndexAPI, GoogleAuth, LoginAPI, CallBackAPI, LogoutAPI

user_routes = Blueprint("user", __name__)
auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

auth_bp.add_url_rule("/login", view_func=LoginAPI.as_view('login'))
auth_bp.add_url_rule("/callback", view_func=CallBackAPI.as_view('callback'))
auth_bp.add_url_rule("/logout", view_func=LogoutAPI.as_view('logout'))


# Route -> Class-based View
user_routes.add_url_rule("/", view_func=IndexAPI.as_view("index_api"))
user_routes.add_url_rule("/users", view_func=UserAPI.as_view("user_api"))

