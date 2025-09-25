from aiogram import types
from loader import dp, bot
from database.db import add_user
from keyboards.inline import join_channels_kb

@dp.message_handler(commands=["start"])
async def start_cmd(message: types.Message):
    args = message.get_args()
    referrer = int(args) if args.isdigit() else None
    add_user(message.from_user.id, referred_by=referrer)

    await message.answer(
        "👋 Welcome to <b>DCON Airdrop Bot</b>!\n\n"
        "To participate, please join the required channels first:",
        reply_markup=join_channels_kb()
    )
