"""test_task_2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path

from settings import settings
from test_task_2 import views

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'', views.index_view),
    path(r'get_map', views.get_map),
    path(r'map', views.map_view),
    path(r'search_map', views.search_map),
    re_path(r'map/(?P<map_id>\d+)/$', views.map_view)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
