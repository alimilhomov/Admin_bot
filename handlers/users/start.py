from aiogram import types 
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup,InputFile,CallbackQuery
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.menu_key import menu1, course ,menukeys
# from aiogram.types import InputFile



from keyboards.inline.menu_key import Menukeybord
from loader import dp

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    photo_file = InputFile(path_or_bytesio="photo/menu_rasm.jpg")
    await message.answer_photo(photo=photo_file, caption="Assalom Aleykum Ilhomov Alimjon botiga xush kelibsiz. Siz bu botda mening loyxam xaqida ma'lumotga ega bo'la olasiz!\n\nDavom etishingiz mumkin",
                        reply_markup=Menukeybord)
    await message.delete()
                        



@dp.callback_query_handler(text='menu')
async def menu_info(call: CallbackQuery):
    photo_file = InputFile(path_or_bytesio="photo/menyu_rasm2.jpg")
    await call.message.answer_photo(photo=photo_file,caption="",
                        reply_markup=menu1)
    await call.message.delete()    



@dp.callback_query_handler(text='about')
async def about_info (call: CallbackQuery):
    photo_file = InputFile(path_or_bytesio="photo/about_pasm.jpg")
    await call.message.edit_media(
        media=types.InputMediaPhoto(photo_file,
        caption=("Asosiy ma'lumotlar:\n\n- Botning ismi: Ilhomov Alimjon\n- Vasiliy Ilhomov\n- Tel. raqami: +998 93 000 00 00\n- Email: ilyhomov@gmail.com")),
        reply_markup=InlineKeyboardMarkup().add(
            InlineKeyboardButton(text='Ortga', callback_data='cansel'),
            InlineKeyboardButton(text="🔗 Bog\'lanish",url="http://t.me/alimilhomov")
        ))



@dp.callback_query_handler(text='cansel')
async def canscel_about(call:CallbackQuery):
    photo_file = InputFile(path_or_bytesio="photo/key_rasm.jpg")
    await call.message.delete()
    await call.message.answer_photo(photo=photo_file, caption="Assosiy menyu",
                        reply_markup=menu1)
    




@dp.callback_query_handler(text='links')
async def Links_about(call:CallbackQuery):
    photo_file = InputFile(path_or_bytesio="photo/links_rasm.jpg")
    await call.message.delete()
    await call.message.answer_photo(photo_file,reply_markup=menukeys)

    



    
@dp.callback_query_handler(text='kurs')
async def Links_about(call:CallbackQuery):
    photo_file = InputFile(path_or_bytesio="photo/kurs_rasm.jpg")
    # await call.message.answer(caption="Tyorlanmoqda")
    await call.message.edit_media(
        media=types.InputMediaPhoto(photo_file,
        caption=("Tayorlanmoqda")),
        reply_markup=InlineKeyboardMarkup().add(
            InlineKeyboardButton(text='Ortga', callback_data='cansel'),
            InlineKeyboardButton(text="🔗 Bog\'lanish",url="http://t.me/alimilhomov")
        ))


@dp.callback_query_handler(text='resume')
async def resume_info(call:CallbackQuery):
    file = InputFile(path_or_bytesio="photo/resume_pdf/resum_pdf2.pdf")
    await call.message.answer_document(
        document=file,
        caption="<b>Ilhomov Alimjon</b>",
        reply_markup=InlineKeyboardMarkup().add(
            InlineKeyboardButton(text='Ortga', callback_data='cansel'),
            # InlineKeyboardButton(text="🔗 Bog\'lanish",url="http://t.me/alimilhomov")
        ))



