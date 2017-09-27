from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.home, name = "home"),
	url(r'^add$', views.add, name = "new_travel"),
	url(r'^create$', views.create, name = "create_travel"),
	url('^show$/(?P<travel_id>\d+)', views.show, name = "show")



]