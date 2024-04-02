from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter()
router.register('', views.BookingViewset)
# router.register('history', views.historyViewset)
urlpatterns = [
    path('', include(router.urls))
]
