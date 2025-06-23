from flask.views import MethodView
# from flask import request, jsonify
from flask import session
from oauthlib.oauth2 import WebApplicationClient
import requests
import json
from flask import current_app, redirect, request, session, url_for


client = WebApplicationClient(None)
def get_google_cfg(app):
    client.client_id = app.config["GOOGLE_CLIENT_ID"]
    return requests.get(app.config["GOOGLE_DISCOVERY_URL"]).json()

class IndexAPI(MethodView):

    def get(self):
        user = session.get("user")
        if user:
            return f"Welcome {user['name']} (<a href='/auth/logout'>Logout</a>)"
        return "<a href='/auth/login'>Login with Google</a>"

class LoginAPI(MethodView):

    def get(self):
        google_auth = GoogleAuth()
        return google_auth.login()

class LogoutAPI(MethodView):

    def get(self):
        google_auth = GoogleAuth()
        return google_auth.logout()

class CallBackAPI(MethodView):

    def get(self):
        google_auth = GoogleAuth()
        google_auth.callback()
        return redirect(url_for("index_api"))


from flask import current_app, redirect, request, session, url_for
from oauthlib.oauth2 import WebApplicationClient
import requests
import json

class GoogleAuth:
    def __init__(self):
        self.client = WebApplicationClient(current_app.config["GOOGLE_CLIENT_ID"])

    def get_provider_cfg(self):
        url = current_app.config["GOOGLE_DISCOVERY_URL"]
        return requests.get(url).json()

    def login(self):
        print("1")
        cfg = self.get_provider_cfg()
        print(cfg, "login is called...")
        auth_endpoint = cfg["authorization_endpoint"]
        request_uri = self.client.prepare_request_uri(
            auth_endpoint,
            redirect_uri=url_for("auth.callback", _external=True),
            scope=["openid", "email", "profile"],
        )
        print(request_uri, "request_uri")
        return redirect(request_uri)

    def callback(self):
        print('call back is calling...')
        code = request.args.get("code")
        
        cfg = self.get_provider_cfg()

        token_url, headers, body = self.client.prepare_token_request(
            cfg["token_endpoint"],
            authorization_response=request.url,
            redirect_url=request.base_url,
            code=code,
        )

        token_response = requests.post(
            token_url,
            headers=headers,
            data=body,
            auth=(
                current_app.config["GOOGLE_CLIENT_ID"],
                current_app.config["GOOGLE_CLIENT_SECRET"],
            ),
        )

        self.client.parse_request_body_response(json.dumps(token_response.json()))

        userinfo_endpoint = cfg["userinfo_endpoint"]
        uri, headers, body = self.client.add_token(userinfo_endpoint)
        userinfo_response = requests.get(uri, headers=headers, data=body)

        user = userinfo_response.json()

        session["user"] = {
            "sub": user["sub"],
            "name": user["name"],
            "email": user["email"],
            "picture": user["picture"],
        }

        # return redirect(url_for("index_api"))

    def logout(self):
        session.clear()
        return redirect(url_for("index_api"))
