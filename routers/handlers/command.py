from aiogram import types, Router
from config.settings import dp, bot
from aiogram.filters import CommandStart, Command
router = Router(name=__name__)

@router.message(CommandStart())
async def start_command(message: types.Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, f"Привет {message.from_user.username}, я бот помощник!\nЕсли хочешь получить свой id вот команда /id")

@router.message(Command(commands=['id'], prefix="!/"))
async def start_command(message: types.Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    await bot.send_message(chat_id, f"Вот твои id\nchat_id:{chat_id}\nuser_id:{user_id}")
