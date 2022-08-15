from django.urls import path
from . import views

urlpatterns = [
	# 'toppage'→'' にしたらドメインの後に何もつけなくてもアクセスできるようになった
	path('', views.toppage, name='toppage'),
	path('owner', views.owner, name='owner'),
	path('updated', views.updated, name='updated'),
]