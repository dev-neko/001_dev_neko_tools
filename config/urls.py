from django.urls import include, path

urlpatterns = [
    path('', include('common_page.urls')),
    path('de_kensaku/', include('de_kensaku.urls')),
]
