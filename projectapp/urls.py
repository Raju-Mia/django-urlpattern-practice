from django.urls import path

from .import views

# this is rerect urls. 
urlpatterns = [
    path('myname/', views.myname, name="myname"),
    path('myage/', views.myage, name="myage"),
]
