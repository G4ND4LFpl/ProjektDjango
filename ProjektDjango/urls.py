"""
Definition of urls for ProjektDjango.
"""

from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from warhammer import views


urlpatterns = [
    path('', views.index, name="index"),

    # Default
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]