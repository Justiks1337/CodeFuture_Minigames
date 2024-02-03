from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.serializers import ModelSerializer

from minigames.gameslist.models import GamesList


class GamesListView(ListAPIView):
    class Serializer(ModelSerializer):
        class Meta:
            model = GamesList
            fields = ['name', 'alias', 'icon', 'url']

    queryset = GamesList.objects.all()
    serializer_class = Serializer
