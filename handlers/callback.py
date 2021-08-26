# (C) supun-maduraga my best friend for his project on call-music-plus

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery
from config import BOT_NAME, BOT_USERNAME, OWNER_NAME, GROUP_SUPPORT, UPDATES_CHANNEL, ASSISTANT_NAME


@Client.on_callback_query(filters.regex("cbstart"))
async def cbback(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>✨ **Welcome {query.message.from_user.mention}** \n
💭 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) 𝗮𝗹𝗹𝗼𝘄 𝘆𝗼𝘂 𝘁𝗼 𝗽𝗹𝗮𝘆 𝗺𝘂𝘀𝗶𝗰 𝗼𝗻 𝗴𝗿𝗼𝘂𝗽𝘀 𝘁𝗵𝗿𝗼𝘂𝗴𝗵 𝘁𝗵𝗲 𝗻𝗲𝘄 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺'𝘀 𝘃𝗼𝗶𝗰𝗲 𝗰𝗵𝗮𝘁𝘀 !**

💡 **𝗙𝗶𝗻𝗱 𝗼𝘂𝘁 𝗮𝗹𝗹 𝘁𝗵𝗲 𝗕𝗼𝘁'𝘀 𝗰𝗼𝗺𝗺𝗮𝗻𝗱𝘀 𝗮𝗻𝗱 𝗵𝗼𝘄 𝘁𝗵𝗲𝘆 𝘄𝗼𝗿𝗸 𝗯𝘆 𝗰𝗹𝗶𝗰𝗸𝗶𝗻𝗴 𝗼𝗻 𝘁𝗵𝗲 » 📚 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀 𝗯𝘂𝘁𝘁𝗼𝗻 !**

❓ **𝗙𝗼𝗿 𝗶𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻 𝗮𝗯𝗼𝘂𝘁 𝗮𝗹𝗹 𝗳𝗲𝗮𝘁𝘂𝗿𝗲 𝗼𝗳 𝘁𝗵𝗶𝘀 𝗯𝗼𝘁, 𝗷𝘂𝘀𝘁 𝘁𝘆𝗽𝗲 /help**
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "➕ Add me to your Group ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],[
                    InlineKeyboardButton(
                        "❓ How to use Me", callback_data="cbguides")
                ],[
                    InlineKeyboardButton(
                         "📚 Commands", callback_data="cbhelp"
                    ),
                    InlineKeyboardButton(
                        "💝 Donate", url=f"https://t.me/{OWNER_NAME}")
                ],[
                    InlineKeyboardButton(
                        "👥 Official Group", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "📣 Official Channel", url=f"https://t.me/{UPDATES_CHANNEL}")
                ],[
                    InlineKeyboardButton(
                        "🌐 Wiki's Page", url="https://github.com/aryazakaria01")
                ],[
                    InlineKeyboardButton(
                        "🧪 Source Code 🧪", url="https://github.com/aryazakaria01/CBMusicBot"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_callback_query(filters.regex("cbhelp"))
async def cbback(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>💡 Hello {query.message.from_user.mention} welcome to the help menu !</b>

**In this menu you can open several available command menus, in each command menu there is also a brief explanation of each command**

⚡ Powered by {BOT_NAME} A.I""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📚 Basic Commands", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "📕 Advanced Commands", callback_data="cbadvanced"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📘 Admin Commands", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "📗 Sudo Commands", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📙 Bot Owner Commands", callback_data="cbowner"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📔 Fun Commands", callback_data="cbfun"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbback(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🏮 Here is the basic commands</b>

🎧 [ GROUP VC CMD ]

/play (song name) - Play song from youtube
/ytp (song name) - Play song directly from youtube 
/stream (reply to audio) - Play song using audio file
/playlist - Show the list song in queue
/song (song name) - Download song from youtube
/search (video name) - Search video from youtube detailed
/vsong (video name) - Download video from youtube detailed
/lyric - (song name) Lyrics scrapper
/vk (song name) - Download song from inline mode

🎧 [ CHANNEL VC CMD ]

/cplay - Stream music on channel voice chat
/cplayer - Show the song in streaming
/cpause - Pause the streaming music
/cresume - Resume the streaming was paused
/cskip - Skip streaming to the next song
/cend - End the streaming music
/admincache - Refresh the admin cache
/ubjoinc - Invite the assistant for join to your channel

⚡ Powered by {BOT_NAME} A.I""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 BACK", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbadvanced"))
async def cbback(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🏮 Here is the advanced commands</b>

/start (in group) - See the bot alive status
/reload - Reload bot and refresh the admin list
/cache - Refresh the admin cache
/ping - Check the bot ping status
/uptime - Check the bot uptime status

⚡ Powered by {BOT_NAME} A.I""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 BACK", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbback(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🏮 Here is the admin commands</b>

/player - Show the music playing status
/pause - Pause the music streaming
/resume - Resume the music was paused
/skip - Skip to the next song
/end - Stop music streaming
/userbotjoin - Invite assistant join to your group
/auth - Authorized user for using music bot
/deauth - Unauthorized for using music bot
/control - Open the player settings panel
/delcmd (on | off) - Enable / disable del cmd feature
/silent - Mute the music player on voice chat
/unsilent - Unmute the music player on voice chat
/musicplayer (on / off) - Disable / enable music player in your group

⚡ Powered by {BOT_NAME} A.I""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 BACK", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbsudo"))
async def cbback(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🏮 Here is the sudo commands</b>

/userbotleaveall - Order the assistant to leave from all group
/gcast - Send a broadcast message trought the assistant
/stats - Show the bot statistic

⚡ Powered by {BOT_NAME} A.I""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 BACK", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbowner"))
async def cbback(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🏮 Here is the owner commands</b>

/stats - Show the bot statistic
/broadcast - Send a broadcast message from bot
/block (user id - duration - reason) - Block user for using your bot
/unblock (user id - reason) - Unblock user you blocked for using your bot
/blocklist - Show you the list of user was blocked for using your bot

📝 Note: all commands owned by this bot can be executed by the owner of the bot without any exceptions.

⚡ Powered by {BOT_NAME} A.I""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 BACK", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbfun"))
async def cbback(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🏮 Here is the fun commands</b>

/chika - Check it by yourself
/wibu - Check it by yourself
/asupan - Check it by yourself
/truth - Check it by yourself
/dare - Check it by yourself

⚡ Powered by {BOT_NAME} A.I""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 BACK", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbguide"))
async def cbback(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ HOW TO USE THIS BOT:

1.) First, add me to your group.
2.) Then promote me as admin and give all permissions except anonymous admin.
3.) Add @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her.
4.) Turn on the voice chat first before start to play music.

⚡ Powered by {BOT_NAME} A.I""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📚 Command List", callback_data="cbhelps"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🗑 Close", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()


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
        
**💡 Feature:** delete every commands sent by users to avoid spam in groups !

**❔ Usage:**

 1️⃣ To turn on feature:
     » type `/delcmd on`
    
 2️⃣ To turn off feature:
     » type `/delcmd off`
      
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


@Client.on_callback_query(filters.regex("cbhelps"))
async def cbback(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>💡 Hello {query.message.from_user.mention} welcome to the help menu !</b>

**In this menu you can open several available command menus, in each command menu there is also a brief explanation of each command**

⚡ Powered by {BOT_NAME} A.I""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📚 Basic Commands", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "📕 Advanced Commands", callback_data="cbadvanced"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📘 Admin Commands", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "📗 Sudo Commands", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📙 Bot Owner Commands", callback_data="cbowner"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📔 Fun Commands", callback_data="cbfun"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🏡 BACK", callback_data="cbguide"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbguides"))
async def cbback(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ HOW TO USE THIS BOT:

1.) First, add me to your group.
2.) Then promote me as admin and give all permissions except anonymous admin.
3.) Add @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her.
4.) Turn on the voice chat first before start to play music.

⚡ Powered by {BOT_NAME} A.I""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 BACK", callback_data="cbstart"
                    )
                ]
            ]
        )
    )
