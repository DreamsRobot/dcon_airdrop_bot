from aiogram import types, Dispatcher
from database.db import SessionLocal
from database.models import User
from config import REF_BONUS

async def profile_cmd(message: types.Message):
    db = SessionLocal()
    user = db.query(User).filter(User.user_id == message.from_user.id).first()
    db.close()
    if not user:
        return await message.answer("❌ You are not registered!")

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton("👤 Profile", callback_data="profile"))
    keyboard.add(types.InlineKeyboardButton("💰 Balance", callback_data="balance"))
    keyboard.add(types.InlineKeyboardButton("📤 Withdraw", callback_data="withdraw"))
    keyboard.add(types.InlineKeyboardButton("👥 Refer", callback_data="refer"))

    await message.answer("🎉 Registration successful!\nChoose an option:", reply_markup=keyboard)

async def callbacks(call: types.CallbackQuery):
    db = SessionLocal()
    user = db.query(User).filter(User.user_id == call.from_user.id).first()

    if call.data == "profile":
        await call.message.answer(f"👤 Name: @{user.username}\n💼 Wallet: {user.wallet or 'Not set'}")

    elif call.data == "balance":
        await call.message.answer(f"💰 Balance: {user.balance} Dcon Coins")

    elif call.data == "withdraw":
        await call.message.answer("🚫 Withdrawal not open yet!")

    elif call.data == "refer":
        ref_link = f"https://t.me/{(await call.bot.me).username}?start={user.user_id}"
        await call.message.answer(f"👥 Referral Link:\n{ref_link}\n\nEach referral = +{REF_BONUS} Dcon Coins")

    db.close()

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(profile_cmd, commands="profile")
    dp.register_callback_query_handler(callbacks, lambda c: c.data in ["profile", "balance", "withdraw", "refer"])
