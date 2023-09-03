from django.urls import path
from userprofile.views import TaskListAPI

urlpatterns = [
    path('tasks/', TaskListAPI.as_view(), name='task-list'),
]