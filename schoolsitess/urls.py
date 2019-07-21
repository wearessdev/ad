"""schoolsitess URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from accounts.API.views import (
    GetAuthToken
)
from rest_framework.routers import DefaultRouter

from accounts.API.views import (
    SSUserViewSet,
    SSUserShortViewSet
)

from feed.API.views import (
    CategoryViewSet,
    ArticleViewSet,
    EventViewSet,
    FeedImageViewSet
)

router = DefaultRouter()
router.register('api/categories', CategoryViewSet)
router.register('api/articles', ArticleViewSet)
router.register('api/events', EventViewSet)
router.register('api/feed-images', FeedImageViewSet)
router.register('api/users', SSUserViewSet)
router.register('api/users-short', SSUserShortViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('api/get-auth-token/', GetAuthToken.as_view())
]

urlpatterns += router.urls
