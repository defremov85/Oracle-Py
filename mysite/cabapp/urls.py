from django.conf.urls import patterns, include, url

from cabapp import views
from cabapp.views import ToolList

urlpatterns = patterns('',
    (r'^$', ToolList.as_view()),
    (r'^refresh.html', views.cp),
)
