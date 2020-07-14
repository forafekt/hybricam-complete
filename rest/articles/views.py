from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from .models import Article
from .forms import ArticleForm
from .serializers import ArticleSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ArticlesListView(APIView):
    """
    List all Articles, or create a new Article.
    """
    def get(self, request, format=None):
        Articles = Article.objects.get_published()
        serializer = ArticleSerializer(Articles, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DraftsListView(APIView):
    """
    List all Draft Articles, or create a new Draft Article.
    """
    def get(self, request, format=None):
        Articles = Article.objects.get_drafts()
        serializer = ArticleSerializer(Articles, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailArticleView(APIView):
    """
    Retrieve, update or delete a Article instance.
    """
    def get_object(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Article = self.get_object(pk)
        serializer = ArticleSerializer(Article)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Article = self.get_object(pk)
        serializer = ArticleSerializer(Article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Article = self.get_object(pk)
        Article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
