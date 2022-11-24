from rest_framework import generics
from posts.models import Post
from api.serializers import PostSerializator


class PostListCreateApi(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializator
    

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)