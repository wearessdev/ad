from rest_framework import viewsets
from services.models import StandardPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response


from ..models import(
    Category,
    Article,
    Event,
    FeedImage
)
from .serializers import(
    CategorySerializer,
    ArticleSerializer,
    EventSerializer,
    FeedImageSerializer
)


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all().order_by('-date_written')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']
    pagination_class = StandardPagination

    @action(detail=True, methods=['post'])
    def like(self, request, pk = None):
        article = Article.objects.get(id=pk)
        return article.like_article()

    @action(detail=True, methods=['post'])
    def love(self, request, pk = None):
        article = Article.objects.get(id=pk)
        return article.love_article()

    @action(detail=True, methods=['post'])
    def dislike(self, request, pk = None):
        article = Article.objects.get(id=pk)
        return article.dislike_article()

    @action(detail=True, methods=['post'])
    def dislove(self, request, pk = None):
        article = Article.objects.get(id=pk)
        return article.dislove_article()

class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all().order_by('-date')
    pagination_class = StandardPagination


class FeedImageViewSet(viewsets.ModelViewSet):
    serializer_class = FeedImageSerializer
    queryset = FeedImage.objects.all().order_by('-date')
    pagination_class = StandardPagination
