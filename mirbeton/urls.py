"""mircouverture URL Configuration

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
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.sitemaps.views import sitemap
from django.conf import settings # new
from django.conf.urls.static import static #new
from siteMain import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', views.index, name='index'),
    re_path(r'^siteMain/', include('siteMain.urls', namespace="siteMain")),
    re_path(r'^antony/', include('antony.urls', namespace="antony")),
    re_path(r'^ales/', include('ales.urls', namespace="ales")),
    re_path(r'^cholet/', include('cholet.urls', namespace="cholet")),
    re_path(r'^chatellerault/',
            include('chatellerault.urls', namespace="chatellerault")),
    re_path(r'^poitiers/',
            include('poitiers.urls', namespace="poitiers")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)
