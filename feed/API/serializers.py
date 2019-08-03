from rest_framework import serializers
from ..models import Category, Article, Event, FeedImage
from accounts.API.serializers import (
    SSUserShortSerializer
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    author_detail = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()

    def get_author_detail(self, obj):
        user = obj.get_author()
        serializer = SSUserShortSerializer(user)
        return serializer.data

    def get_images(self, obj):
        images = obj.get_images()
        serializer = FeedImageSerializer(images, many=True)
        return serializer.data

    class Meta:
        model = Article
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    def get_images(self, obj):
        images = obj.get_images()
        serializer = FeedImageSerializer(images, many=True)
        return serializer.data

    class Meta:
        model = Event
        fields = '__all__'


class FeedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedImage
        fields = '__all__'
