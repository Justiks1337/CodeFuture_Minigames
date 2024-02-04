import asyncio

from database import Connection
from bot_dp import bot, dp
import start


async def main():
    asyncio.create_task(Connection().connect())
    await dp.start_polling(bot)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())



