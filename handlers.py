import os

from main import video_downloader

from aiogram import types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

class DownloadVid(StatesGroup):
    collect_link = State()


async def process_start_command(message: types.Message):
    await DownloadVid.collect_link.set()
    await message.answer("Enter url to download")


async def process_step1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text:
            try:
                file = video_downloader(message.text)
                await message.answer_document(document=open(f'{file[0]}/{file[1]}', 'rb'))
                os.remove(f'{file[0]}/{file[1]}')
                os.rmdir(file[0])
                data.state = None
            except:
                await message.answer("Sorry, but this url is not valid or file size is more than 50 mb. Use /start to try again")
                data.state = None


def register_handlers_core(dp: Dispatcher):
    dp.register_message_handler(process_start_command, commands=["start"])
    dp.register_message_handler(process_step1, state=DownloadVid.collect_link)