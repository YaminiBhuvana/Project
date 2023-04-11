from django.urls import path
from . import views


urlpatterns =[
         path('',views.home, name='home'),
         path('newuser',views.newuser),
         path('login', views.login),
         path('contact',views.contact),
         path('about', views.about),
]