from aiogram import types
from loader import dp
from keyboards.inline import back_kb
from config import BOT_TOKEN

@dp.callback_query_handler(lambda c: c.data == "referral")
async def referral(callback: types.CallbackQuery):
    bot_username = (await dp.bot.me).username
    ref_link = f"https://t.me/{bot_username}?start={callback.from_user.id}"
    text = (
        "👥 <b>Referral System</b>\n\n"
        f"🔗 Your Referral Link:\n{ref_link}\n\n"
        "Invite friends and earn <b>0.2 USDT</b> per successful referral!"
    )
    await callback.message.edit_text(text, reply_markup=back_kb())
