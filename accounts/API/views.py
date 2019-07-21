from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from ..models import SSUser
from rest_framework.response import Response
from ..API.serializers import SSUserSerializer, SSUserShortSerializer


class GetAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(self, GetAuthToken).post(self, request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = SSUser.objects.get(id=token.user_id)
        return Response({'token': token.key, 'user': user})


class SSUserViewSet(viewsets.ModelViewSet):
    queryset = SSUser.objects.all()
    serializer_class = SSUserSerializer


class SSUserShortViewSet(viewsets.ModelViewSet):
    queryset = SSUser.objects.all()
    serializer_class = SSUserShortSerializer
