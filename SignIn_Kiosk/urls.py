"""SignIn_Kiosk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('select_appointment.urls')),
    url(r'', include('registration.urls')),
    url(r'^$',views.front_page, name = 'index'),
    url(r'^sign_in$',views.sign_in, name = 'sign_in'),
    url(r'^help$', views.help_page, name = 'help_page'),
    url(r'^api-access/$', views.api_access, name = 'api_access'),
]
