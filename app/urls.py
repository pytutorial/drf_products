from django.urls import path
from .views import *
from .views_user import *
urlpatterns = [
    path('', index, name='home'),
    path('view_product/<pk>', viewProduct),
    path('purchase/<pk>', purchase),
    path('purchase_confirm/<pk>', purchaseConfirm, name='purchase-confirm'),
    path('thank_you', thankYou, name='thank-you'),
    
    path('signup', signup, name='signup'),
    path('staff', listCategory, name='list-category'),
    path('add_category', addCategory, name='add-category'),
    path('edit_category/<pk>', editCategory, name='edit-category'),
    path('delete_category/<pk>', deleteCategory, name='delete-category'),


    path('list_product', listProduct, name='list-product'),
    path('add_product', addProduct, name='add-product'),
    path('edit_product/<pk>', editProduct, name='edit-product'),
    path('delete_product/<pk>', deleteProduct, name='delete-product'),
]