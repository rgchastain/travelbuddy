from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.home, name = "home"),
	url(r'^add$', views.add, name = "add"),
	url(r'^create$', views.create, name = "create"),
	url(r'^show/(?P<id>\d+)$', views.show, name = "show"),
	url(r'^add_trip/(?P<id>\d+)$', views.add_trip, name = "add_trip"),

]