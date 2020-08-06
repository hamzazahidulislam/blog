from django.urls import path
from .views import *


urlpatterns = [
    path('login/', user_login, name='user-login'),
    path('logout/', user_logout, name='user-logout'),
    path('signup/', user_signup, name='user-singup'),
    path('dashboard/', user_dashboard, name='user-dashboard'),
    path('create-post/', create_post, name='create-post'),
    path('profile/', user_profile, name='profile'),
    path('profile/create-profile/', create_profile, name='create-profile'),
    path('profile/edit-profile/', edit_profile, name='edit-profile'),
]