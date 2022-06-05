import asyncio

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from handlers import register_handlers_core

#Enter your telegram bot token here
TOKEN = "yourtoken"

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher(bot, storage=MemoryStorage())

    register_handlers_core(dp)

    await dp.start_polling()


if __name__ == "__main__":
    asyncio.run(main())
