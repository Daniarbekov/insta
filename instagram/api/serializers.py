from rest_framework import serializers
from posts.models import Post, Comment
from accounts.models import Profile



class CommentsSerializator(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'author','text','created_at']
        read_only_fields = ['id', 'post','author','created_At']


class PostSerializator(serializers.ModelSerializer):
    comments = CommentsSerializator(many=True,read_only=True)
    
    class Meta:
        model = Post
        fields = ['id', 'description', 'author','image','comments','created_at']
        read_only_fields = ['id', 'post','author','created_At','comments']


class AccountSerializator(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Profile
        fields = ['id', 'username', 'email','avatar','first_name','last_name','posts']
        read_only_fields = ['id','posts']