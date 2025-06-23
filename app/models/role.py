from app.extensions import db

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

class UserRole(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    application_id = db.Column(db.Integer, db.ForeignKey('application.id'))

    user = db.relationship("User", backref="roles")
    role = db.relationship("Role")
    application = db.relationship("Application")
