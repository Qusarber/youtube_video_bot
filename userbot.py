import asyncio
from pyrogram import Client

api_id = 12345
api_hash = "yourapphash"


async def send_by_user_bot(chatid, file_name):
    async with Client("my_account", api_id, api_hash) as app:
        async def progress(current, total):
            print(f"{current * 100 / total:.1f}%")

        print(chatid)
        await app.send_video(chat_id='me', video=f'{file_name}', caption="Hi, its your video!", progress=progress)
