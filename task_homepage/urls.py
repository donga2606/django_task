"""task_homepage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from homepage import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/', views.CategoryListView.as_view(), name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('homepage/<pk>/', views.PostListView.as_view(), name="posts_in_category"),
    path('homepage/<pk>/new', views.NewPost.as_view(), name="new_post"),
    path('homepage/<pk>/posts/<post_pk>/edit/', views.PostUpdateView.as_view(), name="edit_post"),
]
