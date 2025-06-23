from app.extensions import db
from datetime import datetime, timedelta

class RefreshToken(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    token = db.Column(db.String(512))
    issued_at = db.Column(db.DateTime, default=datetime.utcnow)
    expires_at = db.Column(db.DateTime)
    is_revoked = db.Column(db.Boolean, default=False)

    user = db.relationship("User", backref="refresh_tokens")
