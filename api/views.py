# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Match, Team, Player
from api.serializers import MatchSerializer, TeamSerializer, PlayerSerializer


@api_view(['GET', 'POST'])
def teams(request):
    if request.method == 'GET':
        serializer = TeamSerializer(Team.objects.all(), many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            team = serializer.save()
            return Response({"team_id": team.pk}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def matches(request):
    if request.method == 'GET':
        serializer = MatchSerializer(Match.objects.all(), many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MatchSerializer(data=request.data)
        if serializer.is_valid():
            match = serializer.save()
            return Response({"match_id": match.pk}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def players(request):
    if request.method == 'GET':
        serializer = PlayerSerializer(Player.objects.all(), many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PlayerSerializer(data=request.data)
        if serializer.is_valid():
            player = serializer.save()
            return Response({"player_id": player.pk}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
