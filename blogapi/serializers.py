from rest_framework import serializers
from blog.models import Post
from users.models import User


class PostS(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    class Meta:
        model = Post
        fields = ['title','description','user','id']


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username','email' ,'posts']