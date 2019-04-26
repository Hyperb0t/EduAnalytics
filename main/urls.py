from django.conf.urls import url
from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^$', views.starter),
    path('starter', views.starter),
    path('main', views.main),
    path('cabinet', views.cabinet),
    path('login', views.loginUser),
    path('logout', views.logoutUser),
    url(r'^graphrestapi/(?P<datatype>[a-z]*)/$', views.graphData)
]
