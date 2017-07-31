from django.conf.urls import url
from general import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
	url(r'^ajax/$', views.ajax, name='ajax'),
	url(r'^ajax2/$', views.ajax2, name='ajax2'),
	url(r'^ajax3/$', views.ajax3, name='ajax3'),
	url(r'^ajax_municipioEncuesta/$', views.ajax_municipioEncuesta, name='ajax_municipioEncuesta'),
	url(r'^$', views.menu_principal, name='menu_principal'),
	url(r'^nueva_ficha/', views.nueva_ficha, name='nueva_ficha'),
	url(r'^ingresar_hijos/(?P<cod_censo>\d+)/(?P<cantidad>\d+)$', views.ingresar_hijos, name='ingresar_hijos'),

	url(r'^nueva_ficha_2/(?P<cod_censo>\d+)$', views.nueva_ficha_2, name='nueva_ficha_2'),
	url(r'^nueva_ficha_3/(?P<cod_censo>\d+)$', views.nueva_ficha_3, name='nueva_ficha_3'),
	url(r'^nueva_ficha_4/(?P<cod_censo>\d+)$', views.nueva_ficha_4, name='nueva_ficha_4'),
	url(r'^nueva_ficha_5/(?P<cod_censo>\d+)$', views.nueva_ficha_5, name='nueva_ficha_5'),
	url(r'^nueva_ficha_6/(?P<cod_censo>\d+)$', views.nueva_ficha_6, name='nueva_ficha_6'),
	url(r'^nueva_ficha_7/(?P<cod_censo>\d+)$', views.nueva_ficha_7, name='nueva_ficha_7'),
	url(r'^nueva_ficha_8/(?P<cod_censo>\d+)$', views.nueva_ficha_8, name='nueva_ficha_8'),	
	url(r'^nueva_ficha_9/(?P<cod_censo>\d+)$', views.nueva_ficha_9, name='nueva_ficha_9'),
	url(r'^nueva_ficha_10/(?P<cod_censo>\d+)$', views.nueva_ficha_10, name='nueva_ficha_10'),
	url(r'^nueva_ficha_11/(?P<cod_censo>\d+)$', views.nueva_ficha_11, name='nueva_ficha_11'),
	url(r'^nueva_ficha_12/(?P<cod_censo>\d+)$', views.nueva_ficha_12, name='nueva_ficha_12'),
	url(r'^nueva_ficha_13/(?P<cod_censo>\d+)$', views.nueva_ficha_13, name='nueva_ficha_13'),
	url(r'^nueva_ficha_14/(?P<cod_censo>\d+)$', views.nueva_ficha_14, name='nueva_ficha_14'),
	url(r'^nueva_ficha_15/(?P<cod_censo>\d+)$', views.nueva_ficha_15, name='nueva_ficha_15'),	
	  
]