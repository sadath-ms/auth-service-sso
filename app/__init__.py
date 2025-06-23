from flask import Flask
from app.config import config_by_name
from app.extensions import db, migrate
from app.routes import register_routes

def create_app(config_name="development"):
    print('calling is:--')
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

    return app
