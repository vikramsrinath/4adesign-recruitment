from django.conf.urls import patterns, url
from component import views


urlpatterns = [
    url(r'^$', views.application_create, name='application_new'),
]
