from app.extensions import db
from datetime import datetime

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    client_id = db.Column(db.String(128), unique=True)
    client_secret = db.Column(db.String(128))
    redirect_uris = db.Column(db.Text)  # JSON or comma-separated
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
