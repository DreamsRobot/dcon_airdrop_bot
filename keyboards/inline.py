from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import REQUIRED_CHANNELS

def join_channels_kb():
    kb = InlineKeyboardMarkup(row_width=1)
    for ch in REQUIRED_CHANNELS:
        kb.add(InlineKeyboardButton(f"Join {ch}", url=f"https://t.me/{ch.strip('@')}"))
    kb.add(InlineKeyboardButton("✅ Done", callback_data="joined"))
    return kb

def main_menu_kb():
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(
        InlineKeyboardButton("👛 Wallet", callback_data="wallet"),
        InlineKeyboardButton("👤 Profile", callback_data="profile"),
    )
    kb.add(
        InlineKeyboardButton("💸 Withdraw", callback_data="withdraw"),
        InlineKeyboardButton("👥 Referral", callback_data="referral"),
    )
    return kb

def back_kb():
    return InlineKeyboardMarkup().add(InlineKeyboardButton("⬅️ Back", callback_data="back"))
