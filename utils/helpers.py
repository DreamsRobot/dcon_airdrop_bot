from aiogram import types
from config import CHANNELS

async def check_subs(message: types.Message, user_id: int):
    for ch in CHANNELS:
        member = await message.bot.get_chat_member(ch, user_id)
        if member.status in ["left", "kicked"]:
            return False
    return True
