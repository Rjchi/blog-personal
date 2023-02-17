from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from apps.category.models import Category

from .serializers import PostSerializer, PostListSerializer
from .models import ViewCount, Post

from .pagination import SmallSetPagination, MediumSetPagination, LargeSetPagination


class BlogListView(APIView):

    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        if Post.objects.all().exists():

            posts = Post.objects.all()

            # Pagination:

            paginator = SmallSetPagination()
            results = paginator.paginate_queryset(posts, request)

            # Many porque van a ser una lista de posts
            serializer = PostListSerializer(results, many=True)

            # return Response({'Post': serializer.data}, status=status.HTTP_200_OK)
            return paginator.get_paginated_response({'posts': serializer.data})
        else:
            return Response({'Error': 'Not posts found'}, status=status.HTTP_404_NOT_FOUND)


class ListPostsByCategoryView(APIView):

    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        if Post.objects.all().exists():

            # Esto es igual a /?category_slug=test ...
            category_slug = request.query_params.get('category_slug')

            # Mostramos los mas nuevos con order_by()
            posts = Post.objects.order_by('-published').all()

            print(category_slug)
            print(posts)
            return Response({'Test': 'Success'}, status=status.HTTP_200_OK)
        else:
            return Response({'Error': 'Not posts found'}, status=status.HTTP_404_NOT_FOUND)
