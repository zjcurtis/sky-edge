import multiprocessing
import time
import urllib.parse
import webbrowser
from base64 import b64encode
from dataclasses import dataclass
from os import getenv

import requests
from dotenv import load_dotenv
from werkzeug import Request, Response, run_simple

load_dotenv()

PORT = 13631
REDIRECT_URI = f"http://localhost:{PORT}/callback"

# TODO these should be loaded from a .env
CLIENT_ID = getenv(key="CLIENT_ID")
APPLICATION_SECRET = getenv(key="APPLICATION_SECRET")
BB_API_SUBSCRIPTION_KEY = getenv(key="BB_API_SUBSCRIPTION_KEY")


@dataclass
class AppTokens:
    access_token: str
    token_type: str
    expires_in: int
    refresh_token: str
    environment_id: str
    environment_name: str
    legal_entity_id: str
    legal_entity_name: str
    user_id: str
    email: str
    family_name: str
    given_name: str
    refresh_token_expires_in: int
    mode: str
    granted_at: float = time.time()

    def access_expired(self) -> bool:
        return self.expires_in + self.granted_at < time.time()

    def refresh_expired(self) -> bool:
        return self.refresh_token_expires_in + self.granted_at < time.time()


def get_token(q: multiprocessing.Queue) -> None:
    @Request.application
    def app(request: Request) -> Response:
        q.put(obj=request.args["code"])
        return Response(response="Good job", status=200)

    run_simple(hostname="localhost", port=PORT, application=app)


def forge_authorization() -> str:
    return f"Basic {b64encode(f'{CLIENT_ID}:{APPLICATION_SECRET}'.encode()).decode()}"


def request_authorization() -> str:
    AUTH_URL = "https://app.blackbaud.com/oauth/authorize"
    params = {
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "response_type": "code",
    }
    url = f"{AUTH_URL}?{urllib.parse.urlencode(query=params)}"
    webbrowser.open(url=url)

    queue = multiprocessing.Queue()
    process = multiprocessing.Process(target=get_token, args=(queue,))
    process.start()
    print("awaiting token")
    token = queue.get(block=True)
    process.terminate()
    return token


def request_token(input: str | AppTokens) -> AppTokens:
    TOKEN_URL = "https://oauth2.sky.blackbaud.com/token"
    body = {}
    headers = {}
    match input:
        case str():
            body = {
                "grant_type": "authorization_code",
                "code": input,
                "redirect_uri": REDIRECT_URI,
                "client_id": CLIENT_ID,
            }
            headers = {
                "authorization": forge_authorization(),
                "Content-Type": "application/x-www-form-urlencoded",
            }
        case AppTokens():
            body = {
                "grant_type": "refresh_token",
                "refresh_token": input.refresh_token,
            }
            headers = {
                "authorization": forge_authorization(),
                "Content-Type": "application/x-www-form-urlencoded",
            }
    response = requests.post(url=TOKEN_URL, data=body, headers=headers).json()
    return AppTokens(**response)
