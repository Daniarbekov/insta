from django.urls import path, include
from .views import PostListCreateApi


urlpatterns = [
    path('', PostListCreateApi.as_view(), name='posts')
]