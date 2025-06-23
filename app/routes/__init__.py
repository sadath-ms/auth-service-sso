from app.routes.user_routes import (
    user_routes,
    auth_bp
)

def register_routes(app):
    app.register_blueprint(user_routes)
    app.register_blueprint(auth_bp)

