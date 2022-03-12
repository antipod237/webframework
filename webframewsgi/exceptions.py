class NotFound(Exceptions):
    code = 404
    text = 'Страница не найдена'

class NotAllowed(Exceptions):
    code = 405
    text = 'Неподдерживаемый http метод'