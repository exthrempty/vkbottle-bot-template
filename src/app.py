from vkbottle.bot import Bot
from vkbottle.tools import load_blueprints_from_package

from src.config import BOT_TOKEN
from src.initialize import setup_db


def init_bot() -> "Bot":
    bot = Bot(token=BOT_TOKEN)
    setup_blueprints(bot)
    setup_middlewares(bot)
    return bot


def setup_blueprints(bot: Bot):
    for bp in load_blueprints_from_package("src/blueprints"):
        bp.load(bot)


def setup_middlewares(bot: Bot):
    for bp in load_blueprints_from_package("src/middlewares"):
        bp.load(bot)


bot = init_bot()
bot.loop_wrapper.on_startup.append(setup_db())
