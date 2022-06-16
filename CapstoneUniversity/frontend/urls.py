from django.urls import path
from .views import index

app_name = 'frontend'

urlpatterns = [
    path('', index, name=''),
    path('register', index),
    path('login', index),
    path('home', index),
    path('students/feed', index),
    
]