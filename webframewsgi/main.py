import re
from typing import List, Type
from webframewsgi.urls import Url
from webframewsgi.exceptions import NotFound
from webframewsgi.views import View


class WebFrame:
    
    __slots__ = ('urls',)

    def __init__(self, urls: List[Url]):
        self.urls = urls

    def __call__(self, environ, start_response):
        view = self._get_view(environ)
        request = self._get_request(environ)
        raw_responce  self._get_responce(environ, view, request)
        responce = raw_responce.encode('utf-8')
        #responce = b"Hello, world\n"
        start_response('200 OK', [
            ('Content-Type', 'text/plain'),
            ('content-Length', str(len(responce)))
        ])
        return iter([responce])

    def _prepare_url(self, url: str):
        if url[-1] == '/':
            return url[:-1]
        return url

    def _find_view(self, raw_url: str) -> Type[View]:
        url = self._prepare_url(raw_url)
        for path in self.urls:
            m = re.match(path.url, url)
            if m is not None:
                return path.view
        raise NotFound

    def _get_view(self, environ, dict) -> View:
        raw_url = environ['PATH_INFO']
        view = self._find_view(raw_url)()
        return view

    def _get_request(self, environ: dict):
        return Request(environ)

    def _get_responce(self, environ: dict):
        method = environ['REQUEST_METHOD'].lower()
        if not hasattr(view, method):
            raise NotAllowed
        return getattr(view, method)(request)