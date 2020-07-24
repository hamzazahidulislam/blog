from django.urls import path
from .views import *


urlpatterns = [
    path('login/', user_login, name ='user-login'),
    path('logout', user_logout, name ='user-logout'),
    path('signup', user_signup, name ='user-singup'),
    path('dashboard', user_dashboard, name ='user-dashboard'),
    path('create-post', create_post, name ='create-post'),
]