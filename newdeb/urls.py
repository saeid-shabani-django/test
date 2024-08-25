from django.urls import  path
from . import  views
urlpatterns = [
    path('<name>/',views.show_deb,name='newdeb'),

]