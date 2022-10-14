


from unicodedata import name
from django.urls import path

from .views import *

urlpatterns = [
    path('myname/', myname, name ='myname'),
    path('myage/', myage, name ='myage'),
    path('<name>/<age>', name, name='name'), #dynamic urls

]