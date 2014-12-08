from django.conf.urls import url

from counter import views

urlpatterns = [
	url(r'^get_visitor_count$', views.get_visitor_count, name='get_visitor_count'),
    url(r'^$', views.index, name='index'),

]