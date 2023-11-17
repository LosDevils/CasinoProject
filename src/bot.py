import asyncio
import logging
from aiogram import Bot, Dispatcher
from src.cfg import config
from api.handlers import (
    start
)
import os
from src.services.database_service import DataBaseService
logging.basicConfig(level=logging.INFO)

config_directory = os.path.dirname(os.path.abspath(config.__file__))
cfg = config.load_config(path=config_directory)
db_service = DataBaseService(cfg.db)
async_session_maker = db_service.get_async_session_maker()
# engine = db_service.create_engine()


async def main():
    bot = Bot(token=cfg.tg_bot.token)
    dp = Dispatcher()
    dp.include_router(start.router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
