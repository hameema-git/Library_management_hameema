from .views import *
from django.urls import path,include
urlpatterns=[
  path("shome/",shome,name='pg1'), 
  path("sbooks/",books,name='pg2'),
  path("home/",home,name='pg3'),
  path('login/',login_view,name="pg4"),
  path("newreg/",signup_view,name='pg5')

]