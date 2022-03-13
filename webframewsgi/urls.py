from dataclasses import dataclass
from webframewsgi.views import View
from typing import Type, Dict, Tuple

@dataclass
class Url:
    url: str
    view: type(View)