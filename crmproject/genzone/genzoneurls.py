from django.urls import re_path
from . import views

urlpatterns=[
    re_path(r'^$',views.index,name='index'),
    re_path(r'^about',views.about,name='about'),
    re_path(r'^registration',views.registration,name='registration'),
    re_path(r'^login',views.login,name='login'),
    re_path(r'^contact',views.contact,name='contact'),
    re_path(r'^saveenq',views.saveenq,name='saveenq'),
    re_path(r'^custreg',views.custreg,name='custreg'),
    re_path(r'^validateuser',views.validateuser,name='validateuser'),
    re_path(r'^adminlogin',views.adminlogin,name='adminlogin'),
    re_path(r'^validateadmin',views.validateadmin,name='validateadmin'),
]
