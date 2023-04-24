from typing import Any
from datetime import datetime

from django.http.request import HttpRequest


def get_context(request: HttpRequest) -> dict[str, Any]:
    """
    Возвращает словарь со значениями по умолчанию, которые отображаются на каждой странице.

    :param request: Запрос пользователя
    :return: Словарь значений по умолчанию
    """
    context = {
        "datetime": datetime.now(),
    }
    if request.user:
        context["user"] = request.user
    return context
