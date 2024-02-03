import aiogram

from config.Config import Config


bot = aiogram.Bot(Config.token)
dp = aiogram.Dispatcher()
