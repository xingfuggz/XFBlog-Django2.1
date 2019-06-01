from django.urls import path, re_path
from . import views


app_name = 'comment'
urlpatterns = [
    path('update_comment/', views.update_comment, name="update_comment"),
]