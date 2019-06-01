from django.urls import path, re_path
from . import views


app_name = 'account'
urlpatterns = [
    path('login/', views.login, name="login"),

]