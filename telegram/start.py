import os

import aiogram.types
from aiogram.filters import CommandStart
from aiogram.types import Message, User
from aiogram.utils.keyboard import InlineKeyboardBuilder
import aiohttp

from bot_dp import bot, dp
from telegram.config.Config import Config


@dp.message(CommandStart())
async def start_handler(message: Message):
    await new_user(message.from_user)

    button = aiogram.types.InlineKeyboardButton(text="Войти в мир игр!",
                                                web_app=aiogram.types.WebAppInfo(url="https://google.com/"))
    await bot.send_message(message.chat.id, "Ссылка 👇", reply_markup=InlineKeyboardBuilder().row(button).as_markup())


async def download_user_avatar(user_id: int):
    """Download user profile photo

    :arg user_id - user id
    """

    user_profile_photo = await bot.get_user_profile_photos(user_id)

    if len(user_profile_photo.photos) > 0:
        file = await bot.get_file(user_profile_photo.photos[0][0].file_id)
        file_destination = get_destination(user_id, get_file_name(file.file_path))
        await bot.download_file(file.file_path, file_destination)

        with open(file_destination, "rb") as destination:
            async with aiohttp.ClientSession() as session:
                async with session.post(
                        f"{Config.http}://{Config.host_name}/users/add_avatar",
                        data={"file": destination},
                        params={"file_name": file_destination,
                                "user_id": user_id},
                        headers={"Authorization": Config.server_authkey}
                ) as response:
                    os.remove(file_destination)


def get_file_name(file_path: str) -> str:
    return file_path[-file_path[::-1].index('/')]


def get_file_format(file_name: str) -> str:
    try:
        return file_name[file_name.index('.'):]
    except ValueError:
        return ".png"


def get_destination(user_id: int, file_name) -> str:
    file_format = get_file_format(file_name)

    file_destination = str(user_id) + file_format

    return file_destination


async def new_user(user: User):
    async with aiohttp.ClientSession() as session:
        async with session.post(f"{Config.http}://{Config.host_name}/users/new_user",
                                headers={"Content-type": "application/json",
                                         "Authorization": Config.server_authkey},
                                params={"user_id": user.id,
                                        "user_fullname": user.full_name,
                                        "username": user.username}) as response:
            json = await response.json()
            if not json["in_database"]:
                await download_user_avatar(user.id)
