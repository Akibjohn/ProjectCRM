from django.urls import re_path
from . import views

urlpatterns=[
    re_path(r'^adminhome',views.adminhome,name='adminhome'),
    re_path(r'^product',views.product,name='product'),
    re_path(r'^customer',views.customer,name='customer'),
    re_path(r'^enquiry',views.enquiry,name='enquiry'),
    re_path(r'^afeedback',views.afeedback,name='afeedback'),
    re_path(r'^acomplain',views.acomplain,name='acomplain'),
    re_path(r'^achangepassword',views.achangepassword,name='achangepassword'),
    re_path(r'^logout',views.logout,name='logout'),
    re_path(r'^adminchangepwd',views.adminchangepwd,name='adminchangepwd'),
    re_path(r'^deletecomplain/(?P<id>\d+)$',views.deletecomplain,name='deletecomplain'),
    re_path(r'^deletefeedback/(?P<id>\d+)$',views.deletefeedback,name='deletefeedback'),
    re_path(r'^deleteenquiry/(?P<id>\d+)$',views.deleteenquiry,name='deleteenquiry'),
    re_path(r'^addnotification',views.addnotification,name='addnotification'),
    re_path(r'^deletenotification/(?P<id>\d+)$',views.deletenotification,name='deletenotification'),
    re_path(r'^addproduct',views.addproduct,name='addproduct'),
    re_path(r'^deleteproduct/(?P<pid>\w+)$',views.deleteproduct,name='deleteproduct'),
    re_path(r'^deletecustomer/(?P<eid>[\w.%+-@2]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$', views.deletecustomer,
        name='deletecustomer'),
]
