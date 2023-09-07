from django.urls import path

from userprofile.api_views import TaskListAPI, TaskViewAPI

urlpatterns = [
    path('all_tasks/', TaskListAPI.as_view(), name='task-list'),
    path('task/<int:pk>/', TaskViewAPI.as_view(), name='single-task'),
]
