from aiogram import types
from loader import dp
from database.db import set_wallet, get_user, update_balance, set_joined
from keyboards.inline import main_menu_kb
from config import JOIN_BONUS, REF_BONUS

@dp.callback_query_handler(lambda c: c.data == "joined")
async def verify_join(callback: types.CallbackQuery):
    # In production, check if user really joined channels
    set_joined(callback.from_user.id)
    update_balance(callback.from_user.id, JOIN_BONUS)

    user = get_user(callback.from_user.id)
    if user[3]:  # if referred_by exists
        update_balance(user[3], REF_BONUS)

    await callback.message.edit_text(
        "✅ Great! Now please submit your <b>BEP-20 wallet address</b>:"
    )

@dp.message_handler(lambda msg: msg.text.startswith("0x"))
async def save_wallet(message: types.Message):
    set_wallet(message.from_user.id, message.text.strip())
    await message.answer(
        "✅ Your wallet has been saved!\n\n🎉 Profile created successfully!",
        reply_markup=main_menu_kb()
    )
