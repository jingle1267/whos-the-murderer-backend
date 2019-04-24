from django.urls import path, include 
from .views import UserViewSet, ImageViewSet, ClueViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'images', ImageViewSet, basename='image')
router.register(r'clues', ClueViewSet, basename='clue')

urlpatterns = router.urls
