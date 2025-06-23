from flask.views import MethodView
from flask import request, jsonify

class UserAPI(MethodView):
    def get(self):
        users = []
        return jsonify([])

    def post(self):
        data = request.json
        email = data.get("email")
        # user = create_user(email)
        return jsonify({"id": 1, "email": 'sadathms007@gmail.com'}), 201
