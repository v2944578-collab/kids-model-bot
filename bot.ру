import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Здравствуйте!\n\n"
        "Это бот детского модельного агентства 👶✨\n\n"
        "Скоро здесь будет запись в группы, расписание и анкеты."
    )


async def main():
    await dp.start_polling(bot)


if name == "__main__":
    asyncio.run(main())
