from django.conf.urls import patterns, include, url

from cabapp.models import Tool

from django.contrib import admin

    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

tool_info = {'model' : Tool}

urlpatterns = [
    url(r'^tools/', include('cabapp.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
