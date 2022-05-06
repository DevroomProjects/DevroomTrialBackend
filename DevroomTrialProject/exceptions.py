from rest_framework import exceptions


class NotFound(exceptions.APIException):

    status_code = '404'

class EnoughtFinance(exceptions.APIException):

    status_code = '400'
    default_detail = 'У вас недостаточно средств'

class PermissionsError(exceptions.APIException):

    status_code = '400'
    default_detail = 'У вас недостаточно прав'

class BadRequest(exceptions.APIException):

    status_code = 400
    default_detail = 'Неизвестная ошибка'