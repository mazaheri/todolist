from django.urls import path

from userprofile.api_views import TaskListAPI, TaskViewAPI, RegistrationView, UserList

urlpatterns = [
    path('all_tasks/', TaskListAPI.as_view(), name='task-list'),
    path('task/<int:pk>/', TaskViewAPI.as_view(), name='single-task'),
    path('signup/', RegistrationView.as_view(), name='signup'),
    path('all_users/', UserList.as_view(), name='all-users')
]
