from django.urls import path
from . import views

urlpatterns = [
    path('toppage', views.toppage, name='toppage'),
    path('owner', views.owner, name='owner'),
    path('updated', views.updated, name='updated'),
]