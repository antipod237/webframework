import os
import re

from webframewsgi.request import Request

class Engine:

    def __init__(self, base_dir: str, template_dir: str):
        self.template_dir = os.path.join(base_dir, template_dir)

    def _get_template_as_string(self, template_name: str):
        template_path = os.path.join(self.template_dir, template_name)
        if not os.path.isfile(template_path):
            raise Exception(f'{template_path} is not file')
        with open(template_name) as f:
            return f.read()

    def _build_block(self, context: dict, raw_template_block: str) ->str:
        