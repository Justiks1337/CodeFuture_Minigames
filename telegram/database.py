import asyncpg

from config.Config import Config


class Connection:

    connection: asyncpg.Connection

    def __new__(cls, *args, **kwargs):
        it = cls.__dict__.get("__it__")
        if it is not None:
            return it
        cls.__it__ = it = object.__new__(cls)
        return it

    @classmethod
    async def connect(cls):
        cls.connection = await asyncpg.connect(
            host=Config.host,
            port=Config.port,
            user=Config.user,
            password=Config.password
        )
