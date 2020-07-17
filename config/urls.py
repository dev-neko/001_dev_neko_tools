from django.urls import include, path

urlpatterns = [
	path('', include('common_page.urls')),
	path('de-kensaku/', include('de_kensaku.urls')),
	path('dev-fd36c01ask/',include('dev.urls')),
]
