from datetime import datetime
from webframewsgi.view import View
from webframewsgi.request import Request
from webframewsgi.response import Response
from webframewsgi.template_engine import build_template

class Homepage(View):

    def get(self, request, *args, **kwargs):
        body = build_template(request, {'time': str(datetime.now()), 'lst': [1,2,3]}, 'home.html')
        return Response(body=body)

class EpicMath(View):

    def get(self, request: Request, *args, **kwargs):
        first = request.GET.get('first')
        if not first or not first[0].isnumeric():
            return Response(body = f'first пустое либо не является числом')

        second = request.GET.get('second')
        if not second or not second[0].isnumeric():
            return Response(body = f'second пустое либо не является числом')
        
        return Response(body = f'Сумма {first[0]} и {second[0]} = {int(first[0]) + int(second[0])}')