from django.conf.urls import url

from counter import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]