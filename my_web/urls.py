from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.article_list, name='article_list'),
    path('article/<slug:slug>/', views.article_detail, name='article_detail'),
    path('register/', views.registration, name='register'),
    path('confirm-email/', views.confirm_email, name='confirm_email'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('comment/<int:article_id>/', views.add_comment, name='add_comment'),
    path('search/', views.search_news, name='search_news'),
]