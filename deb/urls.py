from django.urls import path
from . import views

urlpatterns = [
    path('deb/<int:id>/',views.show_deb,name='deb'),
]
