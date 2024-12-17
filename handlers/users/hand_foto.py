from loader import dp, bot
from aiogram.types import ContentTypes,Message
from pathlib import Path
from aiogram import types


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def get_file_id_p(message: types.Message):
    await message.reply(message.photo[-1].file_id)
