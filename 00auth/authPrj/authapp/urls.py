# from django.urls import path, re_path, include
# from django.contrib.auth import views as auth_views
# from social_django.urls import urlpatterns as social_django_urls

# urlpatterns = [
#     # ...
#     path('auth/', include('social_django.urls', namespace='social')),
#     path('authapp/', include('authapp.urls')),
#     path('google/callback/', views.profile, name='profile'),
#     # ...
# ]

# 📁 authapp/urls.py -----

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("callback", views.callback, name="callback"),
]