from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_attempt, name='login_attempt'),
    path('register/', register_attempt, name='register_attempt'),
    path('token', token_send, name = 'token_send'),
    path('success', success, name = 'success'),
    path('verify/<auth_token>', verify, name = 'verify'),
    path('error', error_page, name='error'),
    path('dashboard/', dashboard, name='dashboard'), 
    path('logout', logout_attempt, name='logout_attempt'),
    path('change_password', change_password, name='change_password')
]
