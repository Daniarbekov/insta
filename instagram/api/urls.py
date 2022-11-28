from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostListCreateApi

router = DefaultRouter()
router.register(r'posts', PostListCreateApi,basename="posts")



urlpatterns = [
    path('', include(router.urls)),
]