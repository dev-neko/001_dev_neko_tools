from django.urls import path
from . import views

urlpatterns = [
	path('ya_src_tool/',views.ya_src_tool),
	path('ya_src_tool/output', views.output)
]
