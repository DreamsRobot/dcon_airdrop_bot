import logging
from aiogram import Bot, Dispatcher, executor, types
from config import BOT_TOKEN
from handlers import start, wallet, profile, referral, admin
from database.db import Base, engine

# Logging
logging.basicConfig(level=logging.INFO)

# Init bot
bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

# DB setup
Base.metadata.create_all(bind=engine)

# Register handlers
start.register_handlers(dp)
wallet.register_handlers(dp)
profile.register_handlers(dp)
referral.register_handlers(dp)
admin.register_handlers(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
