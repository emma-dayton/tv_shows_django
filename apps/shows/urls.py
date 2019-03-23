from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index),
  url(r'^shows$', views.shows),
  url(r'^shows/new$', views.shows_new),
  url(r'^shows/create$', views.shows_create),
  url(r'^shows/(?P<num>\d+)$', views.show_info),
  url(r'^shows/(?P<num>\d+)/edit$', views.show_edit),
  url(r'^shows/(?P<num>\d+)/update$', views.show_update),
  url(r'^shows/(?P<num>\d+)/destroy$', views.show_destroy),
]
