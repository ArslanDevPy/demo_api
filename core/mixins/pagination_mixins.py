from rest_framework import pagination


class CustomPaginationBY3(pagination.PageNumberPagination):
    page_size = 3
