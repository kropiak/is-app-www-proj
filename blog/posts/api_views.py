from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Topic, Category, Post
from .serializers import TopicSerializer, CategoryModelSerializer, PostModelSerializer


# określamy dostępne metody żądania dla tego endpointu
@api_view(['GET'])
def topic_list(request):
    """
    Lista wszystkich obiektów modelu Topic.
    """
    if request.method == 'GET':
        topics = Topic.objects.all()
        # many=True oznacza zwrócenie wielu instancji obiektu, a nie tylko jednego (lista)
        serializer = TopicSerializer(topics, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def topic_detail(request, pk):

    """
    :param request: obiekt DRF Request
    :param pk: id obiektu Topic
    :return: Response (with status and/or object/s data)
    """
    try:
        topic = Topic.objects.get(pk=pk)
    except Topic.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    """
    Zwraca pojedynczy obiekt typu Topic.
    """
    if request.method == 'GET':
        topic = Topic.objects.get(pk=pk)
        serializer = TopicSerializer(topic)
        return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
# @authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def topic_update_delete(request, pk):

    """
    :param request: obiekt DRF Request
    :param pk: id obiektu Topic
    :return: Response (with status and/or object/s data)
    """
    try:
        topic = Topic.objects.get(pk=pk)
    except Topic.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # dodajemy nowy obiekt Topic
    if request.method == 'PUT':
        serializer = TopicSerializer(topic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # usuwanie obiektu Topic
    elif request.method == 'DELETE':
        topic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def find_topic_by_keyword(request, keyword):
    topics = Topic.objects.filter(name__icontains=keyword)
    serializer = TopicSerializer(topics, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def category_list(request):
    """
    Lista wszystkich obiektów modelu Category.
    """
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategoryModelSerializer(categories, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def category_detail(request, pk):

    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        category = Category.objects.get(pk=pk)
        serializer = CategoryModelSerializer(category)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CategoryModelSerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'POST':
        serializer = CategoryModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer
