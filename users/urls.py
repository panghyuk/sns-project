from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('<int:id>/mypage',views.mypage,name='mypage'),
    path('<int:id>/follow',views.follow,name='follow'),
]