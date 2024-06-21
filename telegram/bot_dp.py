import aiogram

from telegram.config.Config import Config


bot = aiogram.Bot(Config.token)
dp = aiogram.Dispatcher()
