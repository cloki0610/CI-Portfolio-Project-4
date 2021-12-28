""" Theme URL """
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
