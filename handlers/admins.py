from asyncio import QueueEmpty
from cache.admins import set
from pyrogram import Client, filters
from pyrogram.types import Message
from callsmusic import callsmusic
from callsmusic.queues import queues
from helpers.channelmusic import get_chat_id
from helpers.filters import command, other_filters
from helpers.decorators import errors, authorized_users_only
from config import BOT_USERNAME, que, admins

@Client.on_message(command(["reload", f"reload@{BOT_USERNAME}"]) & other_filters)
@errors
@authorized_users_only
async def update_admin(client, message: Message):
    chat_id = get_chat_id(message.chat)
    set(
        chat_id,
        [
            member.user
            for member in await message.chat.get_members(filter="administrators")
        ],
    )
    await message.reply_text("✔ Bot **ʀᴇʟᴏᴀᴅᴇᴅ ᴄᴏʀʀᴇᴄᴛʟʏ !**\n\n• **ᴀᴅᴍɪɴ ʟɪsᴛ** ʜᴀs ʙᴇᴇɴ **ᴜᴘᴅᴀᴛᴇᴅ.**")


@Client.on_message(command(["pause", f"pause@{BOT_USERNAME}"]) & other_filters)
@errors
@authorized_users_only
async def pause(_, message: Message):
    chat_id = get_chat_id(message.chat)
    if (chat_id not in callsmusic.pytgcalls.active_calls) or (
        callsmusic.pytgcalls.active_calls[chat_id] == "paused"
    ):
        await message.reply_text("☣ ɴᴏᴛʜɪɴɢ ɪs ᴘʟᴀʏɪɴɢ!")
    else:
        callsmusic.pytgcalls.pause_stream(chat_id)
        await message.reply_text("➤ ᴍᴜsɪᴄ ᴘᴀᴜsᴇᴅ!")


@Client.on_message(command(["resume", f"resume@{BOT_USERNAME}"]) & other_filters)
@errors
@authorized_users_only
async def resume(_, message: Message):
    chat_id = get_chat_id(message.chat)
    if (chat_id not in callsmusic.pytgcalls.active_calls) or (
        callsmusic.pytgcalls.active_calls[chat_id] == "playing"
    ):
        await message.reply_text("☣ ɴᴏᴛʜɪɴɢ ɪs ᴘᴀᴜsᴇᴅ!")
    else:
        callsmusic.pytgcalls.resume_stream(chat_id)
        await message.reply_text("✈ ᴍᴜsɪᴄ ʀᴇsᴜᴍᴇᴅ!")


@Client.on_message(command(["end", f"end@{BOT_USERNAME}"]) & other_filters)
@errors
@authorized_users_only
async def stop(_, message: Message):
    chat_id = get_chat_id(message.chat)
    if chat_id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text("☣ ɴᴏᴛʜɪɴɢ ɪɴ sᴛʀᴇᴀᴍɪɴɢ!")
    else:
        try:
            callsmusic.queues.clear(chat_id)
        except QueueEmpty:
            pass

        callsmusic.pytgcalls.leave_group_call(chat_id)
        await message.reply_text("✘ ᴍᴜsɪᴄ sᴛᴏᴘᴘᴇᴅ!")


@Client.on_message(command(["skip", f"skip@{BOT_USERNAME}"]) & other_filters)
@errors
@authorized_users_only
async def skip(_, message: Message):
    global que
    chat_id = get_chat_id(message.chat)
    if chat_id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text("☣ ɴᴏᴛʜɪɴɢ ᴛᴏ sᴋɪᴘ!")
    else:
        callsmusic.queues.task_done(chat_id)

        if callsmusic.queues.is_empty(chat_id):
            callsmusic.pytgcalls.leave_group_call(chat_id)
        else:
            callsmusic.pytgcalls.change_stream(
                chat_id, callsmusic.queues.get(chat_id)["file"]
            )
            
    qeue = que.get(chat_id)
    if qeue:
        skip = qeue.pop(0)
    if not qeue:
        return
    await message.reply_text(f"➤ sᴋɪᴘᴘᴇᴅ : **{skip[0]}**\n➤ ɴᴏᴡ ᴘʟᴀʏɪɴɢ : **{qeue[0][0]}**")


@Client.on_message(filters.command("cache"))
@errors
async def admincache(client, message: Message):
    set(
        message.chat.id,
        [
            member.user
            for member in await message.chat.get_members(filter="administrators")
        ],
    )
    await message.reply_text("✔ **ᴀᴅᴍɪɴ ᴄᴀᴄʜᴇ** ɪs **ʀᴇғʀᴇsʜᴇᴅ**")
