from pyrogram.types import Message
from pyrogram import Client

api_id = 12345
api_hash = "yourapihash"

async def send_by_user_bot(user_username, file_name):
    async with Client("my_account", api_id, api_hash) as app:
        async def progress(current, total):
            print(f"{current * 100 / total:.1f}%")
        await app.send_video(chat_id=user_username, video=f'{file_name}', caption="Hi, its your video!", progress=progress)
