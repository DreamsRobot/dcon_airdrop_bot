from aiogram import types, Dispatcher
from config import CHANNELS, START_BALANCE
from database.db import SessionLocal
from database.models import User
from utils.helpers import check_subs

async def start_cmd(message: types.Message):
    db = SessionLocal()
    user = db.query(User).filter(User.user_id == message.from_user.id).first()
    if not user:
        ref_id = None
        if len(message.text.split()) > 1:
            try:
                ref_id = int(message.text.split()[1])
            except:
                pass
        user = User(
            user_id=message.from_user.id,
            username=message.from_user.username,
            balance=START_BALANCE,
            referred_by=ref_id
        )
        db.add(user)
        db.commit()
    db.close()

    keyboard = types.InlineKeyboardMarkup()
    for ch in CHANNELS:
        keyboard.add(types.InlineKeyboardButton(f"Join {ch}", url=f"https://t.me/{ch[1:]}"))
    keyboard.add(types.InlineKeyboardButton("✅ Done", callback_data="check_subs"))

    await message.answer("🚀 <b>Dcon Airdrop Coming Soon</b>\n\nJoin required channels to continue.", reply_markup=keyboard)

async def check_callback(call: types.CallbackQuery):
    ok = await check_subs(call.message, call.from_user.id)
    if not ok:
        await call.answer("❌ You must join all channels!", show_alert=True)
        return
    await call.message.delete()
    await call.message.answer("✅ You joined all channels!\n\nPlease submit your BEP-20 Wallet Address:")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_cmd, commands="start")
    dp.register_callback_query_handler(check_callback, text="check_subs")
