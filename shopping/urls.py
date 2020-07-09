from django.contrib import auth
from django.urls import path

from . import views
from django.urls import path



urlpatterns = [
    path('', views.my_home, name='my_home'),
    path('des_movie/<int:id>/', views.des_movie, name='des_movie'),
    path('report/', views.report, name='report'),
    path('buy/<int:id>/', views.buy, name='buy'),

    ]
