from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.norm_url_patterns if hasattr(admin.site, 'norm_url_patterns') else admin.site.urls), # standard or just path('admin/', admin.site.urls)
    path('api/', include('traffic_app.urls')),
]
