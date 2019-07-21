from rest_framework import viewsets
from services.models import StandardPagination

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
    pagination_class = StandardPagination


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all().order_by('-date')
    pagination_class = StandardPagination


class FeedImageViewSet(viewsets.ModelViewSet):
    serializer_class = FeedImageSerializer
    queryset = FeedImage.objects.all().order_by('-date')
    pagination_class = StandardPagination
