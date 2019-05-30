from rest_framework import serializers
from apis.posts.models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'body', 'author')


class CommentSerializer(serializers.ModelSerializer):
    post = PostSerializer()

    class Meta:
        models = Comment
        fields = ('post', 'comment', 'commented_by')


