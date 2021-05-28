from rest_framework.serializers import ModelSerializer
from .models import *

class BlogSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class BlogUserSerializer(ModelSerializer):
    class Meta:
        model = BlogUser
        fields = '__all__'

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
