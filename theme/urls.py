""" Theme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from . import views


urlpatterns = [
    path('new_theme/', views.NewThemeView.as_view(), name='new_theme'),
    path('<slug:slug>/', views.ThemeOverView.as_view(),
         name='theme_overview'),
    path('edit_theme/<slug:slug>/',
         views.EditThemeView.as_view(), name='edit_theme'),
    path('delete_theme/<slug:slug>/', views.DeleteTheme.as_view(),
         name='delete_theme'),
    path('theme_upvote/<int:theme_pk>/', views.ThemeUpvote.as_view(),
         name='theme_upvote'),
    path('theme_downvote/<int:theme_pk>/', views.ThemeDownvote.as_view(),
         name='theme_downvote'),
    path('<slug:slug>/post/', include('post.urls')),
    path('<slug:slug>/report/', include('report.urls')),
]
