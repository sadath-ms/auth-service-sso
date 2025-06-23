from flask import Flask
from app.config import config_by_name
from app.extensions import db, migrate
from app.routes import register_routes

def create_app(config_name="development"):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    db.init_app(app)
    migrate.init_app(app, db)
    from app.models import (
    user,
    identity,
    role,
    application,
    session,
    token
)
    register_routes(app)
    # app.route("/")
    # def index():
    #     print('index is calling ...')
    #     user = session.get("user")
    #     if user:
    #         return f"Welcome {user['name']} (<a href='/auth/logout'>Logout</a>)"
    #     return "<a href='/auth/login'>Login with Google</a>"
    return app
