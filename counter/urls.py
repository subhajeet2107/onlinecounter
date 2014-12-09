from django.conf.urls import url

from counter import views

urlpatterns = [
	url(r'^get_visitor_count$', views.get_visitor_count, name='get_visitor_count'),
	url(r'^end_session$', views.end_session, name='end_session'),
	url(r'^get_current_ip$', views.get_current_ip, name='get_current_ip'),
    url(r'^$', views.index, name='index'),

]