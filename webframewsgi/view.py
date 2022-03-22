from webframewsgi.request import Request
from webframewsgi.response import Response

class View:
    def get(self, request: Request, *args, **kwargs) -> Response:
        pass
    
    def post(self, request: Request, *args, **kwargs) -> Response:
        pass