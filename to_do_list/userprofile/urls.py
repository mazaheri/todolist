from django.urls import path

from userprofile.views import profile, login, signup

# these urls are using for django templates
# api urls are in api_urls.py
urlpatterns = [
    path('', profile, name='hi'),
    path("login/", login, name="login"),
    # path("sign-up/", signup, name="sign-up")
]
