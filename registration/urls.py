from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^register/(?P<a_id>\d+)$', views.register_screen, name='register_screen'),
    url(r'^register/(?P<a_id>\d+)/basic_info$', views.basic_info, name='basic_info'),
    url(r'^register/(?P<a_id>\d+)/details$', views.details, name='details'),
]