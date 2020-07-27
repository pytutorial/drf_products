from django.urls import path
from .views_api import *
urlpatterns = [
    path('hello', hello),
    path('get_category_list', getCategoryList),
    path('search_product', searchProduct),
    path('product_detail/<pk>', getProductDetail),

    path('order_products', orderProducts),
]