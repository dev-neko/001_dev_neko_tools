from django.urls import path
from . import views

urlpatterns = [
	path('',views.input,name='de_kensaku_input'),
	path('output',views.output,name='de_kensaku_output'),
]