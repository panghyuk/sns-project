from django.urls import path
from .views import *

app_name = "main"

urlpatterns = [
    path('',showmain,name='home'),
    path('who/',who,name='who'),
    path('what/',what,name='what'),
    path('future/',future,name='future'),
    path('posts/', posts, name="posts"),
    path('<str:id>',detail,name = 'detail'),
    path('new/',new,name='new'),
    path('create/',create,name='create'),
    path('edit/<str:id>',edit,name="edit"),
    path('update/<str:id>',update,name='update'),
    path('delete/<str:id>',delete,name='delete'),
]