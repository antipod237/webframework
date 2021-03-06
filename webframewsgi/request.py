from urllib.parse import parse_qs

class Request:

    def __init__(self, environ: dict, settings: dict):
        self.buid_get_params_dict(environ['QUERY_STRING'])
        self.build_post_params_dict(environ['wsgi.input'].read())
        self.environ = environ
        self.settings = settings
        self.extra = {}

    def __getattr__(self, item):
        return self.extra.get(item)

    
    def buid_get_params_dict(self, raw_params: str):
        self.GET = parse_qs(raw_params)

    def build_post_params_dict(self, raw_bytes: bytes):
        raw_params = raw_bytes.decode('UTF-8')
        self.POST = parse_qs(raw_params)
