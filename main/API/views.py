from rest_framework import viewsets
from ..models import Team, Roster
from .serializers import TeamSerializer, RosterSerializer
from services.models import StandardPagination


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    pagination_class = StandardPagination


class RosterViewSet(viewsets.ModelViewSet):
    queryset = Roster.objects.all()
    serializer_class = RosterSerializer
    pagination_class = StandardPagination
