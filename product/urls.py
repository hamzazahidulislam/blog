from django.urls import path
from  .views import *
urlpatterns = [
    path('',product_list,name='product-list'),
    path('<int:id>',product_detail,name='product_detail'),
    path('filter/<str:filter>',product_filter,name='product_filter'),
    path('price/<int:price>',product_price,name='product_filter'),


]
