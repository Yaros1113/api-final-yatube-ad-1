from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response


class CustomLimitOffsetPagination(LimitOffsetPagination):
    """
    Кастомная пагинация: возвращает список, если нет параметров
    limit/offset.
    """

    def paginate_queryset(self, queryset, request, view=None):
        # Проверяем, есть ли параметры пагинации в запросе
        if ('limit' not in request.query_params
                 and 'offset' not in request.query_params):
            return None  # Не пагинируем, если параметры не указаны

        return super().paginate_queryset(queryset, request, view)

    def get_paginated_response(self, data):
        # Возвращаем пагинированный словарь, только если использовали пагинацию
        return Response({
            'count': self.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data
        })
