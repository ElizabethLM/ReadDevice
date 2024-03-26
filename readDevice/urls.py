from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Uncomment the next line to enable the admin:
    
    path('device/', include('device.urls')),
    path('admin/', admin.site.urls)
]
