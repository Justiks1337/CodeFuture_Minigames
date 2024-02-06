from django.shortcuts import render
from django.http import HttpRequest
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


async def index(request: HttpRequest):
    return render(request, 'gameslist/gameslist.html')
