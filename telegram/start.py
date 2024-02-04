import aiogram.types
from aiogram.filters import CommandStart
from aiogram.types import Message, User
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot_dp import bot, dp
from database import Connection
from config.Config import Config


@dp.message(CommandStart())
async def start_handler(message: Message):
    if not await in_database(message.from_user.id):
        await new_user(message.from_user)

    button = aiogram.types.InlineKeyboardButton(text="Войти в мир игр!", web_app=aiogram.types.WebAppInfo(url="https://google.com/"))
    await bot.send_message(message.chat.id, "Ссылка 👇", reply_markup=InlineKeyboardBuilder().row(button).as_markup())


async def __download_user_avatar(user_id: int):
    """Download user profile photo

    :arg user_id - user id
    """

    user_profile_photo = await bot.get_user_profile_photos(user_id)

    if len(user_profile_photo.photos) > 0:

        file = await bot.get_file(user_profile_photo.photos[0][0].file_id)
        file_destination = get_destination(user_id, get_file_name(file.file_path))
        await bot.download_file(file.file_path, file_destination)


def get_file_name(file_path: str) -> str:
    return file_path[-file_path[::-1].index('/'):]


def get_file_format(file_name: str) -> str:
    return file_name[file_name.index('.'):]


def get_destination(user_id: int, file_name) -> str:

    file_format = get_file_format(file_name)

    file_destination = Config.avatars + str(user_id) + file_format

    return file_destination


def get_name(user: User) -> str:
    if not user.username:
        return user.first_name if not user.last_name else f"{user.first_name} {user.last_name}"
    return user.username


async def in_database(user_id: int) -> bool:
    return bool(await Connection().connection.fetchrow(
        "SELECT user_id FROM users WHERE user_id = $1",
        user_id))


async def new_user(user: User):
    await __download_user_avatar(user.id)
    await Connection().connection.execute("INSERT INTO users VALUES ($1, $2)", user.id, get_name(user))
