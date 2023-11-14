from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page),
    path('home', views.index_page),
    path('get_data', views.get_data),
    path('form', views.form),
    path('find_char', views.find_char),
]