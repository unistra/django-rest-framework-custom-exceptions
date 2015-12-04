from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = patterns('',
    url(r'^items', views.ItemList.as_view()),
    url(r'^not-items', views.NotItemList.as_view()),
    url(r'^forbidden-items', views.ForbiddenItemList.as_view()),
)
