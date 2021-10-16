from django.urls import path, include
from . import views
from rest_framework import routers
from . import api_views as record_api_views

router = routers.DefaultRouter()
router.register('todo', record_api_views.TodoViewSet)

app_name= 'todo'

urlpatterns = [
    # viewsからindexを読み込んで、nameをindexに
    path('', views.index, name='index'),
    path('<int:pk>', views.todo_detail, name='todo_detail'),
    path('create', views.todo_create, name='todo_create'),
    path('update/<int:pk>', views.todo_update, name='todo_update'),
    path('delete/<int:pk>', views.todo_delete, name='todo_delete'),
    path('api/', include(router.urls)),
]