from rest_framework import viewsets
from posts.models import Post
from api.serializers import PostSerializator


class PostListCreateApi(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializator
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)