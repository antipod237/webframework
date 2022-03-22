from urllib.parse import parse_qs

class Request:

    def __init__(self, environ: dict, settings: dict):
        self.buid_get_params_dict(environ['QUERY_STRING'])
        self.settings = settings
    
    def buid_get_params_dict(self, raw_params: str):
        self.GET = parse_qs(raw_params)