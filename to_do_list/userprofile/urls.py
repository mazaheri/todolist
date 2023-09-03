from django.urls import path

from userprofile.views import profile


urlpatterns = [
    path('', profile, name='hi'),
]
