from django.urls import path
from . import views

urlpatterns = [
	path('slider', views.slider, name='slider'),
	path('slider/surprise/',views.for_ajax),
]