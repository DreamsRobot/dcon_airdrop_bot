from aiogram import executor
from loader import dp
from database.db import init_db

# Import all handlers
import handlers.start
import handlers.profile
import handlers.referral
import handlers.wallet

async def on_startup(_):
    print("✅ Dcon Airdrop Bot is starting...")
    init_db()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
