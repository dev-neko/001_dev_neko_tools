from django.urls import include, path
from django.contrib import admin

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include('common_page.urls')),
	# path('dev-fd36c01ask/',include('dev.urls')),
	path('de_kensaku/',include('de_kensaku.urls')),
	path('support-parts-gen/',include('support_parts_gen.urls')),
]