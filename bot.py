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
        "👋 Мы - не просто детское модельное агентство\n\n"
        "Мы - ALFAkids. Мы помогаем детям раскрыть уверенность, харизму и любовь к сцене ✨\n\n"
        "📸 Модельная походка\n"
        "🎭 Актёрское мастерство\n"
        "🗣 Работа с речью и камерой\n\n"
        "Выберите нужный раздел в меню ниже ⬇️",
        reply_markup=main_menu
    )



async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())


if __name__ == "__main__":
    asyncio.run(main())
