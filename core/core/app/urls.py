from django.urls import path
from . import views


urlpatterns = [
    path('post_list/', views.post_list, name='post_list'),
    path('index/', views.index, name='index'),
    path('post_detail/<int:pk>/', views.post_detail, name='post_detail'),
    path('post_create/', views.post_create, name='post_create'),
    path('post_delete/<int:pk>/', views.post_delete, name='post_delete'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
