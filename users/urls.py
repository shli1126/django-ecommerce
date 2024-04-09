from django.urls import path
from .views import register, login
app_name = "core"
urlpatterns = [
    path("register/", register, name="register"),
    path("login/", login, name="login"),
]