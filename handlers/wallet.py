from aiogram import types, Dispatcher
from database.db import SessionLocal
from database.models import User

async def wallet_handler(message: types.Message):
    db = SessionLocal()
    user = db.query(User).filter(User.user_id == message.from_user.id).first()
    if not user:
        db.close()
        return
    user.wallet = message.text.strip()
    db.commit()
    db.close()

    await message.answer(f"✅ Wallet saved!\n\n💼 Address: <code>{message.text}</code>\n\nRegistration successful! 🎉\nUse /profile to see details.")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(wallet_handler, lambda m: m.text.startswith("0x"))
