from django.conf.urls import url
from interface import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', views.login, name='login'),
    url(r'^usuario/$', views.usuario, name='usuario'),
]
