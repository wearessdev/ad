from django.db import models
from ckeditor.fields import RichTextField
from accounts.models import SSUser

# Create your models here.


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'categories'

    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Article(models.Model):
    name = models.CharField(max_length=80)
    author = models.ForeignKey(SSUser, on_delete=models.CASCADE)
    date_written = models.DateTimeField(auto_now=True)
    content = RichTextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    is_published = models.BooleanField(default=True)
    publish_date = models.DateTimeField()
    like = models.IntegerField()
    love = models.IntegerField()

    def get_author(self):
        return self.author

    def get_images(self):
        return self.feedimage_set.all()

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=80)
    description = RichTextField()
    date = models.DateTimeField()
    location = models.TextField()
    like = models.IntegerField()
    love = models.IntegerField()

    def get_images(self):
        return self.feedimage_set.all()

    def __str__(self):
        return self.name


class FeedImage(models.Model):
    name = models.CharField(max_length=80)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    caption = models.CharField(max_length=120)
    file = models.ImageField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name






