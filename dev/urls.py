from django.urls import path
from . import views

urlpatterns = [
	path('slider', views.slider, name='slider'),
	path('slider/for_ajax/',views.for_ajax),
	path('kihu_parts_gen/', views.kihu_parts_gen, name='kihu_parts_gen'),
	path('modal01/', views.modal01),
	path('tame/',views.tame),
]