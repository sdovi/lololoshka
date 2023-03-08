from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('about', views.mymac, name='btn1'),
    path('main', views.main)

]
