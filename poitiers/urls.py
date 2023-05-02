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

app_name = 'poitiers'

urlpatterns = [
    re_path(r'^$', views.indexPoitiers, name='indexPoitiers'),
    re_path(r'^services/$', views.pageServices, name='pageServices'),
    re_path(r'^articles/$', views.pageArticles, name='pageArticles'),
    # -------------------------     Articles Pages       --------------------------
    re_path(r'^article-1/$', views.pageArticle_1, name='pageArticle_1'),
    # -------------------------     Services Pages       --------------------------
    re_path(r'^service-1/$', views.pageService_1, name='pageService_1'),
    re_path(r'^bordure-beton-poitiers/$', views.pageServiceBordureBeton,
            name='pageServiceBordureBeton'),
    re_path(r'^beton-cire-poitiers/$', views.pageServiceBetonCire,
            name='pageServiceBetonCire'),
    re_path(r'^dalle-beton-poitiers/$', views.pageServiceDalleBeton,
            name='pageServiceDalleBeton'),
    re_path(r'^beton-decoratif-poitiers/$',
            views.pageServiceBetonDecoratif, name='pageServiceBetonDecoratif'),
    re_path(r'^beton-desactive-poitiers/$',
            views.pageServiceBetonDesactive, name='pageServiceBetonDesactive'),
    re_path(r'^beton-imprime-poitiers/$', views.pageServiceBetonImprime,
            name='pageServiceBetonImprime'),
    re_path(r'^bitume-enrobe-poitiers/$', views.pageServiceBitumeEnrobe,
            name='pageServiceBitumeEnrobe'),
    re_path(r'^coulage-fondation-poitiers/$',
            views.pageServiceCoulageFondation, name='pageServiceCoulageFondation'),
    re_path(r'^pavage-dallage-poitiers/$', views.pageServicePavageDallage,
            name='pageServicePavageDallage'),
    re_path(r'^resine-sol-epoxy-poitiers/$',
            views.pageServiceResineEpoxy, name='pageServiceResineEpoxy'),
    re_path(r'^terrasse-gres-cerame-poitiers/$',
            views.pageServiceGresCerame, name='pageServiceGresCerame'),
    re_path(r'^terrasse-pierre-naturelle-poitiers/$',
            views.pageServicePierreNaturelle, name='pageServicePierreNaturelle'),
    re_path(r'^terrasse-pierre-naturelle-gres-cerame-poitiers/$',
            views.pageServicePierreNaturelleGresCerame, name='pageServicePierreNaturelleGresCerame'),
    re_path(r'^amenagement-exterieur-poitiers/$',
            views.pageServiceAmenagementExterieur, name='pageServiceAmenagementExterieur'),
    re_path(r'^terrasse-bois-poitiers/$',
            views.pageServiceTerrasseBois, name='pageServiceTerrasseBois'),

    # -------------------------     Thank You Pages       --------------------------
    re_path(r'^thank-you/$', views.thankYouPoitiers,
            name='thankYouPoitiers'),
    # -------------------------     Promotion Pages       --------------------------
    re_path(r'^promotion-du-printemps/$',
            views.pagePoitiersPromotionDuPrintemps, name='pagePoitiersPromotionDuPrintemps'),
    re_path(r'^promotion-du-printemps-thank-you/$', views.thankYouPoitiersPromotionDuPrintemps,
            name='thankYouPoitiersPromotionDuPrintemps'),
    # -------------------------     GDPR Pages       --------------------------
    re_path(r'^mentionslegales/$', views.mentions_lega, name='mentions_lega'),
    re_path(r'^politiquedeconfidentialite/$',
            views.politique_conf, name='politique_conf'),
    re_path(r'^politiquedecookies/$',
            views.politique_cook, name='politique_cook'),
]
