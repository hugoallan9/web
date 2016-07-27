from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url('^tipo_cambio$', 'apps.tipo_cambio.views.tipo_cambio')
]
