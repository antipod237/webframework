from dataclasses import dataclass
from webframewsgi.view import View
from typing import Type

@dataclass
class Url:
    url: str
    view: type(View)