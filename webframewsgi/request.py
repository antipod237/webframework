from urllib.parse import parse_qs

class Request:

    def __call__(self, environ: dict):
        pass
    
    def buid_get_params_dict(self, raw_responce: str):
        self.GET = parse_qs(raw_responce)