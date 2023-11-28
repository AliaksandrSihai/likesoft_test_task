from rest_framework.pagination import PageNumberPagination


class ListPagination(PageNumberPagination):
    """ Пагинация для вывода """
    page_size = 5
    page_size_query_param = 'page'
    max_page_size = 100
