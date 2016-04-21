from rest_framework import serializers

from blog.models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title','text', 'author', 'published_date')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('post', 'text', 'author', 'created_date', 'likes', 'dislikes')
