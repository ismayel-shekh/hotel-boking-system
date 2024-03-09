from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter()
router.register('list', views.HotelViewSet)
router.register('catagory', views.CategoryViewSet)
router.register('review', views.ReviewViewSet)
urlpatterns = [
    path('', include(router.urls))
]
