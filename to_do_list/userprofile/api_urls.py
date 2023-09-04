from django.urls import path
from userprofile.views import TaskListAPI

urlpatterns = [
    path('', TaskListAPI.as_view(), name='task-list'),

]