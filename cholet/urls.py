"""paysageHortica URL Configuration

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
from . import views

app_name = 'cholet'

urlpatterns = [
    re_path(r'^$', views.indexCholet, name='indexCholet'),
    re_path(r'^services/$', views.pageServices, name='pageServices'),
    re_path(r'^articles/$', views.pageArticles, name='pageArticles'),
    # -------------------------     Articles Pages       --------------------------
    re_path(r'^article-1/$', views.pageArticle_1, name='pageArticle_1'),
    # -------------------------     Services Pages       --------------------------
    re_path(r'^service-1/$', views.pageService_1, name='pageService_1'),
    re_path(r'^bordure-beton-cholet/$', views.pageServiceBordureBeton,
            name='pageServiceBordureBeton'),
    re_path(r'^beton-cire-cholet/$', views.pageServiceBetonCire,
            name='pageServiceBetonCire'),
    re_path(r'^dalle-beton-cholet/$', views.pageServiceDalleBeton,
            name='pageServiceDalleBeton'),
    re_path(r'^beton-decoratif-cholet/$',
            views.pageServiceBetonDecoratif, name='pageServiceBetonDecoratif'),
    re_path(r'^beton-desactive-cholet/$',
            views.pageServiceBetonDesactive, name='pageServiceBetonDesactive'),
    re_path(r'^beton-imprime-cholet/$', views.pageServiceBetonImprime,
            name='pageServiceBetonImprime'),
    re_path(r'^bitume-enrobe-cholet/$', views.pageServiceBitumeEnrobe,
            name='pageServiceBitumeEnrobe'),
    re_path(r'^coulage-fondation-cholet/$',
            views.pageServiceCoulageFondation, name='pageServiceCoulageFondation'),
    re_path(r'^pavage-dallage-cholet/$', views.pageServicePavageDallage,
            name='pageServicePavageDallage'),
    re_path(r'^resine-sol-epoxy-cholet/$',
            views.pageServiceResineEpoxy, name='pageServiceResineEpoxy'),
    re_path(r'^terrasse-gres-cerame-cholet/$',
            views.pageServiceGresCerame, name='pageServiceGresCerame'),
    re_path(r'^terrasse-pierre-naturelle-cholet/$',
            views.pageServicePierreNaturelle, name='pageServicePierreNaturelle'),

    # -------------------------     Thank You Pages       --------------------------
    re_path(r'^thank-you/$', views.thankYouCholet, name='thankYouCholet'),
    # -------------------------     GDPR Pages       --------------------------
    re_path(r'^mentionslegales/$', views.mentions_lega, name='mentions_lega'),
    re_path(r'^politiquedeconfidentialite/$',
            views.politique_conf, name='politique_conf'),
    re_path(r'^politiquedecookies/$',
            views.politique_cook, name='politique_cook'),
]
