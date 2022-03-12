import re
from typing import List
from webframewsgi.urls import Url
from webframewsgi.exceptions import NotFound
from webframewsgi.view import View


class WebFrame:

    __slots__ = ('urls',)

    def __init__(self, urls):
        self.urls = urls

    def __call__(self, environ, start_response):
        data = b"Hello, world\n"
        start_response('200 OK', [
            ('Content-Type', 'text/plain'),
            ('content-Length', str(len(data)))
        ])
        return iter([data])

        def _prepare_url(self, url: str):
            if url[-1] == '/':
                return url[:-1]
            return url

        def _find_view(self, raw_url: str) -> Type(View):
            url = self._prepare_url(raw_url))
            for path in self.urls:
                m = re.match(path.url, url)
                if m is not None:
                    return path.view
                raise NotFound