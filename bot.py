from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
import asyncio
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Здравствуйте!\n\n"
        "Это бот детского модельного агентства 🧸✨\n\n"
        "Выберите нужный раздел в меню 👇"
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
