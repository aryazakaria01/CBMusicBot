# (C) supun-maduraga my best friend for his project on call-music-plus

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery
from config import BOT_NAME


# close calllback

@Client.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()

# Player Control Callbacks

@Client.on_callback_query(filters.regex("cbback"))
async def cbback(_, query: CallbackQuery):
    await query.edit_message_text(
        "**💡 Here is the control menu of bot:**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⏸ Pause music", callback_data="cbpause"
                    ),
                    InlineKeyboardButton(
                        "▶️ Resume music", callback_data="cbresume"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⏩ Skip music", callback_data="cbskip"
                    ),
                    InlineKeyboardButton(
                        "⏹ End music", callback_data="cbend"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔇 Mute player", callback_data="cbmute"
                    ),
                    InlineKeyboardButton(
                        "🔊 Unmute player", callback_data="cbunmute"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🗑 Del cmd", callback_data="cbdelcmds"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbdelcmds"))
async def cbdelcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>This is the feature information:</b>
        
**💡 Feature:** delete every commands sent by users to avoid spam !

**❔ Usage:**

   1️⃣ To turn on feature:
      - type /delcmd on
    
   2️⃣ To turn off feature:
      - type /delcmd off
      
⚡ Powered by {BOT_NAME} A.I""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 BACK", callback_data="cbback"
                    )
                ]
            ]
        )
    )
