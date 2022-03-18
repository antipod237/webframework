from webframewsgi.views import View

class Homepage(View):

    def get(self, request, *args, **kwargs):
        return 'hello world from view'

class EpicMath(View):

    def get(self, request: Request, *args, **kwargs):
    first = request.GET('first')
    if not first or not first[0].isnumeric():
        return f'first пустое либо не является числом'

    second = request.GET('second')
    if not second or not second[0].isnumeric():
        return f'second пустое либо не является числом'

    return f'Сумма {first[0]} и {second[0]} = {int(first[0]) + int(second[0])}'