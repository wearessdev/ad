from rest_framework import serializers
from ..models import Team, Roster, Player, SeasonSchedule, ScheduleItem


class TeamSerializer(serializers.ModelSerializer):
    roster = serializers.SerializerMethodField()

    def get_roster(self, obj):
        roster = obj.get_roster()
        serializer = RosterSerializer(roster, many=True)
        return serializer.data

    class Meta:
        model = Team
        fields = '__all__'


class RosterSerializer(serializers.ModelSerializer):
    players_list = serializers.SerializerMethodField()

    def get_players_list(self, obj):
        players_list = obj.get_players()
        serializer = PlayerSerializer(players_list, many=True)
        return serializer.data

    class Meta:
        model = Roster
        fields = '__all__'


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

class SeasonScheduleSerializer(serializers.ModelSerializer):
    schedule_items = serializers.SerializerMethodField()

    def get_schedule_items(self, obj):
        schedule_items = obj.get_schedule_items()
        serializer = ScheduleItemSerializer(schedule_items, many=True )
        return serializer.data

    class Meta:
        model = SeasonSchedule
        fields = '__all__'

class ScheduleItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleItem
        fields = '__all__'
