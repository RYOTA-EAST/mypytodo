from django.urls import path
from . import views

app_name= 'todo'
urlpatterns = [
    # viewsからindexを読み込んで、nameをindexに
    path('', views.index, name='index'),
]