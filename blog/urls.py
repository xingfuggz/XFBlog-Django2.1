from django.urls import path, re_path
from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('category/<int:category_id>/', views.category_list, name="category"),
    path('detail/<int:article_id>/', views.detail_blog, name="detail"),
    path('dates/<int:year>/<int:month>/', views.blog_with_dates, name="dates"),
    path('read_nums/', views.read_num_s, name="read_nums")  # 统计计数页面
]