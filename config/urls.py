from django.urls import include, path
from django.contrib import admin

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include('common_page.urls')),
	path('de-kensaku/', include('de_kensaku.urls')),
	path('dev-fd36c01ask/',include('dev.urls')),
	path('work_apps/',include('work_apps.urls')),
	path('work_apps/accounts/',include('django.contrib.auth.urls')),
]