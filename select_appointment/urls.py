from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^select_appointment$', views.select_screen, name='select_screen'),
]