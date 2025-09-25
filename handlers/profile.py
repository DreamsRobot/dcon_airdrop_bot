from aiogram import types
from loader import dp
from database.db import get_user
from keyboards.inline import main_menu_kb, back_kb

@dp.callback_query_handler(lambda c: c.data == "profile")
async def show_profile(callback: types.CallbackQuery):
    user = get_user(callback.from_user.id)
    if user:
        text = (
            f"👤 <b>Your Profile</b>\n\n"
            f"🆔 User ID: <code>{user[0]}</code>\n"
            f"👛 Wallet: {user[1] or 'Not set'}\n"
            f"💰 Balance: {user[2]} USDT\n"
            f"👥 Referred By: {user[3] or 'None'}"
        )
        await callback.message.edit_text(text, reply_markup=back_kb())
