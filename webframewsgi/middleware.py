from webframewsgi.request import Request
from webframewsgi.response import Response
from uuid import uuid4
from urllib.parse import parse_qs

class BaseMiddleware:

    def to_request(self, request: Request):
        return

    def to_response(self, response: Response):
        return

class Session(BaseMiddleware):
    
    def to_response(self, response: Response):
        if not response.request.session_id:
            response.update_headers(
                {'Set-Cookie': f'session_id={uuid4()}' }
            )

middlewares = {
    Session
}