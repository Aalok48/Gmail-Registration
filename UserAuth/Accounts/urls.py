from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('login', login_attempt, name='login_attempt'),
    path('register', register_attempt, name='register_attempt')
]
