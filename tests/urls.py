from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^items', views.ItemList.as_view()),
    url(r'^not-items', views.NotItemList.as_view()),
    url(r'^forbidden-items', views.ForbiddenItemList.as_view()),
]
