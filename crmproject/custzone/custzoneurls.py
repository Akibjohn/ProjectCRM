from django.urls import re_path
from . import views

urlpatterns=[
    re_path(r'^custhome',views.custhome,name='custhome'),
    re_path(r'^viewproducts',views.viewproducts,name='viewproducts'),
    re_path(r'^complain',views.complain,name='complain'),
    re_path(r'^feedback',views.feedback,name='feedback'),
    re_path(r'^changepassword',views.changepassword,name='changepassword'),
    re_path(r'^logout',views.logout,name='logout'),
    re_path(r'^raisecomplain',views.raisecomplain,name='raisecomplain'),
    re_path(r'^givefeedback',views.givefeedback,name='givefeedback'),
    re_path(r'^changepwd',views.changepwd,name='changepwd'),
]