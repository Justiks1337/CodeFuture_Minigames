from django.shortcuts import render
from django.http.request import HttpRequest
from asgiref.sync import sync_to_async

from minigames.gameslist.models import GamesList


async def index(request: HttpRequest, **kwargs):
    try:
        await sync_to_async(GamesList.objects.get)(alias=(kwargs['tag']))
        return await sync_to_async(render)(request, 'games_queue/queue.html')

    except GamesList.DoesNotExist:
        return await sync_to_async(render)(request, 'errorpage.html')
