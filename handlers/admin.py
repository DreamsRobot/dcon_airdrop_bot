from aiogram import types, Dispatcher
from config import ADMIN_IDS
from database.db import SessionLocal
from database.models import User

async def broadcast(message: types.Message):
    if message.from_user.id not in ADMIN_IDS:
        return
    text = message.text.split(" ", 1)[1]
    db = SessionLocal()
    users = db.query(User).all()
    db.close()

    sent = 0
    for u in users:
        try:
            await message.bot.send_message(u.user_id, text)
            sent += 1
        except:
            pass
    await message.answer(f"✅ Broadcast sent to {sent} users.")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(broadcast, commands="broadcast", commands_prefix="/")
