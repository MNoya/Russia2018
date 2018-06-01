from rest_framework import serializers
from models import Match, Player, Group, Lineup, Changes, Event, Team


class TeamSerializer(serializers.ModelSerializer):
    """
    {
        "country": "Uruguay"
    }
    """

    class Meta:
        model = Team
        fields = ('id', 'country',)


class MatchSerializer(serializers.ModelSerializer):
    """
    {
        "winner": 1,
        "team1": 1,
        "team2": 2
    }
    """

    class Meta:
        model = Match
        fields = ('id', 'team1', 'team2', 'winner',)


class PlayerSerializer(serializers.ModelSerializer):
    """
    {
        "name": "Suarez",
        "position": "striker-goalkeeper",
        "number": 9,
        "team": 1
    }
    """

    class Meta:
        model = Player
        fields = ('id', 'name', 'position', 'number', 'team')
