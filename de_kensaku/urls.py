from django.urls import path
from . import views

urlpatterns = [
	path('', views.input, name='de-kensaku-input'),
	path('output', views.output, name='de-kensaku-output'),
]