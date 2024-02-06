from urllib.parse import parse_qs

import aiohttp
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from asgiref.sync import sync_to_async

from minigames.gameslist.models import GamesList
from minigames.games_queue.models import Users
from config.Config import Config


class PlayerWebsocket(AsyncJsonWebsocketConsumer):

    consumers = {}

    @classmethod
    async def add_to_consumer_group(cls, consumer):
        """Добавление в группу cls.consumers

        cls.consumers хранилище всех потребителей разделенные на группы,
        в зависимости от очереди в которой они находятся

        """

        if not cls.consumers.get(consumer.group):
            if not await cls.create_consumer_group(consumer.group):
                return False

        if not cls.player_in_database(consumer.user_id):
            return False

        cls.consumers.get(consumer.group).append(consumer)
        return True

    @classmethod
    async def create_consumer_group(cls, consumer: str):
        """Create consumers group in cls.consumers"""

        if await cls.game_in_database(consumer):
            cls.consumers[consumer] = []
            return True
        return False

    @classmethod
    async def game_in_database(cls, game: str):
        """Existence check"""

        try:
            await sync_to_async(GamesList.objects.get)(alias=game)
            return True
        except GamesList.DoesNotExist:
            return False

    @classmethod
    async def player_in_database(cls, user_id: int):
        """Existence check"""

        try:
            await sync_to_async(Users.objects.get)(user_id=user_id)
            return True
        except Users.DoesNotExist:
            return False

    async def connect(self):
        self.group = self.scope['url_route']['kwargs']['tag']
        self.user_id = (await self.get_params())['user_id'][0]

        if await self.accept():
            if await self.get_player_count() == await self.get_maximum_player():
                await self.start_game_send(await self.start_game())

        await self.new_user_count()

    async def disconnect(self, code):
        await self.close(code=code)
        await self.new_user_count()

    async def start_game(self):

        game = GamesList.objects.get(alias=self.group)

        async with aiohttp.ClientSession() as session:
            async with session.get(
                    f'https://{game._domain}/api/v1/start_game',
                    headers={
                        'players': [i.user_id for i in PlayerWebsocket.consumers[self.group]],
                        'Authorization': Config.server_authkey}) as response:
                print((await response.json())['url'])
                return (await response.json())['url']

    async def new_user_count(self):
        await self.channel_layer.group_send(
            self.group,
            {
                'type': 'user.count',
                'count': await self.get_player_count(),
                'max_size': await self.get_maximum_player()
             })

    async def user_count(self, event):
        await self.send_json({
            'type': 'user_count',
            'count': event["count"],
            'max_size': event["max_size"]
        })

    async def start_game_send(self, url):
        await self.channel_layer.group_send(
            self.group,
            {
                'type': 'start_game_event',
                'url': url
             })

    async def start_game_event(self, event):
        await self.send_json({
            'type': 'start_game_event',
            'url': event['url']
        })

    async def accept(self, subprotocol=None):
        if not await PlayerWebsocket.add_to_consumer_group(self):
            await self.disconnect(404)
            return False

        await self.channel_layer.group_add(
            self.group,
            self.channel_name
        )
        await super().accept()
        return True

    async def close(self, code=None):
        await self.channel_layer.group_discard(
            self.group,
            self.channel_name
        )

        await sync_to_async(PlayerWebsocket.consumers[self.group].remove)(self.user_id)

        await super().close(code=code)

    async def get_player_count(self) -> int:
        return await sync_to_async(len)(PlayerWebsocket.consumers[self.group])

    async def get_maximum_player(self) -> int:
        return (await sync_to_async(GamesList.objects.get)(alias=self.group)).max_size

    async def get_params(self):
        return await sync_to_async(parse_qs)(self.scope['query_string'].decode())
