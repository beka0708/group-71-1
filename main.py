import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from src.handlers import router


BOT_TOKEN = "8649581342:AAHClU2K22UI-qY1AA6sw_woZN3MlB83veE"


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())     # обработчик входящих обновлений


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)     # отправляет запросы на тг-сервер



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
