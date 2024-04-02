
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('customer.urls')),
    path('hotel/', include('hotels.urls')),
    path('booking/', include('history.urls')),
    path('contact_us/', include('contact_us.urls')),
    path('deposit/', include('All_update.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)