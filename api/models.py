# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Team(models.Model):
    country = models.CharField(max_length=100, unique=True)


class Group(models.Model):
    code = models.CharField(max_length=1)
    teams = models.ManyToManyField(Team)


class Player(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=20)
    number = models.IntegerField()
    team = models.ForeignKey(Team)


class Match(models.Model):
    team1 = models.ForeignKey(Team, related_name='team1')
    team2 = models.ForeignKey(Team, related_name='team2')
    score1 = models.PositiveIntegerField()
    score2 = models.PositiveIntegerField()


class Lineup(models.Model):
    team = models.ForeignKey(Team)
    match = models.ForeignKey(Match)
    players = models.ManyToManyField(Player)


class Changes(models.Model):
    lineup = models.ForeignKey(Lineup)
    player_in = models.ForeignKey(Player, related_name='player_in')
    player_out = models.ForeignKey(Player, related_name='player_out')
    minute = models.IntegerField()


class Event(models.Model):
    name = models.CharField(max_length=20)
    player = models.ForeignKey(Player)
    minute = models.IntegerField()
    seconds = models.IntegerField()
    match = models.ForeignKey(Match)
