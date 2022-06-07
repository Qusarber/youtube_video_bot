import os

from main import (
    video_downloader,
    video_quality,
)
from userbot import send_by_user_bot

from aiogram import types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import (
    KeyboardButton,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)


class DownloadVid(StatesGroup):
    collect_link = State()
    collect_quality = State()


async def process_start_command(message: types.Message):
    await DownloadVid.collect_link.set()
    await message.answer("Enter url to download")


async def process_step0(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text:
            data['collect_link'] = message.text
            available_resolurion = video_quality(message.text)
            kb = ReplyKeyboardMarkup(resize_keyboard=True)
            for i in available_resolurion:
                kb.add(KeyboardButton(i))
            await message.answer("Please, select quality of video", reply_markup=kb)
            await DownloadVid.next()


async def process_step1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        available_resolurion = video_quality(data['collect_link'])
        if message.text in available_resolurion:
            kb = ReplyKeyboardRemove()
            try:
                file = video_downloader(data['collect_link'], message.text)
                file_path_and_name = f'{file[0]}/{file[1]}'
                await message.answer_document(document=open(file_path_and_name, 'rb'))
                os.remove(file_path_and_name)
                os.rmdir(file[0])
                data.state = None
            except:
                try:
                    await message.answer("We need a few more time to process your request because video size is more than 50 MB. We will send you video into private chat.", reply_markup=kb)
                    await send_by_user_bot(message.from_user.id, file_path_and_name)
                    await message.answer("File was sent to your private chat")
                    os.remove(file_path_and_name)
                    os.rmdir(file[0])
                    data.state = None
                except:
                    await message.answer("Something went wrong. Try again via /start", reply_markup=kb)
                    os.remove(file_path_and_name)
                    os.rmdir(file[0])
                    data.state = None
        else:
            await message.answer("Please, select quality of video from keyboard")


def register_handlers_core(dp: Dispatcher):
    dp.register_message_handler(process_start_command, commands=["start"])
    dp.register_message_handler(process_step0, state=DownloadVid.collect_link)
    dp.register_message_handler(process_step1, state=DownloadVid.collect_quality)