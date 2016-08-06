from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', 'system.views.home', name = "home"),

    url(r'^carlist/$', 'system.views.car_list', name = "car_list"),
    url(r'^createOrder/$', 'system.views.order_created', name = "order_create"),

    url(r'^(?P<id>\d+)/edit/$', 'system.views.car_update', name = "car_edit"),


    url(r'^(?P<id>\d+)/$', 'system.views.car_detail', name = "car_detail"),
    url(r'^detail/(?P<id>\d+)/$', 'system.views.order_detail', name = "order_detail"),

    url(r'^(?P<id>\d+)/delete/$', 'system.views.car_delete', name = "car_delete"),
    url(r'^(?P<id>\d+)/deleteOrder/$', 'system.views.order_delete', name = "order_delete"),

    url(r'^contact/$', 'system.views.contact', name = "contact"),

    url(r'^newcar/$', 'system.views.newcar', name = "newcar"),
    url(r'^(?P<id>\d+)/like/$', 'system.views.like_update', name = "like"),
    url(r'^popularcar/$', 'system.views.popular_car', name = "popularcar"),

]
