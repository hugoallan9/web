from django.conf.urls import url
from django.contrib import admin
from views import *

urlpatterns = [
    url('^tipo_cambio$',tipo_cambio),
]
