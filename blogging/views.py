from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

#endpoint describing home view
@api_view(['GET'])
def home_view(request):
    return Response({
        '/blogs(GET,POST)':'All blogs',
        '/comments(GET,POST)':'All comments'
    })

#API to create and list blogs
@api_view(['GET','POST'])
def blogs(request):
    if request.method == 'GET':
        content = Blog.objects.all()
        serializer = BlogSerializer(content,many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = BlogSerializer(data=request.data,many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

#api to create and list comments
@api_view(['GET','POST'])
def comments(request):
    if request.method == 'GET':
        serializer = CommentSerializer(Comment.objects.all(),many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data,many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


