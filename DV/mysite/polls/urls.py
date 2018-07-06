
from django.conf.urls import url, include
from django.contrib import admin
from . import views


urlpatterns = [
	url(r'^home/', views.home, name='home'),
	url(r'^prueba/', views.prueba, name='prueba'),
	url(r'^prueba2/', views.prueba2, name='prueba2')
]	


	