"""
Definition of urls for ProjektDjango.
"""

from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from warhammer import views
#from django.conf import settings
#from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name="index"),

    # Default
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)