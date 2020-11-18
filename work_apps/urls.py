from django.urls import path
from . import views

urlpatterns = [
	path('ya_src_tool/',views.ya_src_tool),
	path('ya_src_tool/output', views.output),
	path('ya_src_tool_v2/',views.ya_src_tool_v2),
	path('ya_src_tool_v2/output_v2',views.output_v2),
]
