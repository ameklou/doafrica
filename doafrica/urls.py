from django.conf.urls import url

from . import views

urlpatterns= [
	url(r'^$', views.index, name='index'),
	url(r'^signin$', views.signin, name='signin'),
	url(r'^conlogin$', views.conlogin, name='conlogin'),
	url(r'^profil$', views.profil, name='profil'),
	url(r'^conlogout$', views.conlogout, name='conlogout'),
	url(r'^edit_profil$', views.edit_profil, name='edit_profil'),
	url(r'^photo$', views.photo, name='photo'),
    url(r'^association$',views.association, name='association'),
    url(r'^admin$',views.admin, name='admin'),
]