from app.extensions import db
from datetime import datetime

class Identity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    provider = db.Column(db.String(50))  # 'google', 'github', etc.
    provider_uid = db.Column(db.String(255))
    email = db.Column(db.String(120))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship("User", backref="identities")
