from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='index'),
    path('detail/<int:post_id>', post_detail, name='post-detail'),
]