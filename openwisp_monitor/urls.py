"""openwisp_monitor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin, auth
from django.conf.urls import include
from django.views.generic.base import RedirectView
from django_cas_ng.views import login, logout, callback

urlpatterns = [
    url(r'^$', RedirectView.as_view(pattern_name='devices_home', permanent=True), name='index'),
    url(r'^devices/', include('devices.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #url('^', include('django.contrib.auth.urls')),
    #url(r'^login', auth.views.login, {'template_name': 'registration/login.html'}, name='login'),
    #url(r'^logout', auth.views.logout, {'next_page': '/login'}, name='logout'),
    #url(r'^login', login, {'next_page': '/devices'}, name='login'),
    #url(r'^logout', logout, {'next_page': '/login'}, name='logout'),

    url(r'^accounts/login$', login, name='cas_ng_login'),
    url(r'^accounts/logout$', logout, name='cas_ng_logout'),
    url(r'^accounts/callback$', callback, name='cas_ng_proxy_callback'),

    url(r'^collectd_rest/', include('collectd_rest.urls')),
    # ... other urls in your project ...
    url(r'^', include('django_x509.urls', namespace='x509')),

    # controller URLs
    # used by devices to download/update their configuration
    # keep the namespace argument unchanged
    url(r'^', include('django_netjsonconfig.controller.urls', namespace='controller')),
    # common URLs
    # shared among django-netjsonconfig components
    # keep the namespace argument unchanged
    url(r'^', include('django_netjsonconfig.urls', namespace='netjsonconfig')),
]
