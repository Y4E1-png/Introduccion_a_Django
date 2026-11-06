from rest_framework.pagination import PageNumberPagination

class ProductPagination (PageNumberPagination):
  page_size=25
  page_query_param = "p"
  page_size_query_param = "size"
  max_page_size= 50
  last_page_strings= ("end",)