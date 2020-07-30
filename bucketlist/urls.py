from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='bucket-list-home'),
    path('add/', views.get_input, name='bucket-list-get-input')
]


