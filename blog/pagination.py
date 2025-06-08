from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class BlogCustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 50

    def get_paginated_response(self, data):
        return Response({
            "count": self.page.paginator.count,
            "next": self.get_next_link(),
            "previous": self.get_previous_link(),
            "results": data,
            "page_number": self.get_page_number(self.request, self),
            "num_pages": self.page.paginator.num_pages,
        })
