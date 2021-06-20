from django.urls import path
from . import views

urlpatterns = [
	path('', views.input, name='support-parts-gen-input'),
]