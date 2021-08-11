# Copyright (C) 2021 VeezProject
# Veez Music Project

import io
import os

from pyrogram import filters
from tswift import Song

from pyrogram import Client as veez

@veez.on_message(filters.command(["lyric", "lyrics"]))
async def _(client, message):
    lel = await message.reply("__searching lyrics...__")
    query = message.text
    if not query:
        await lel.edit("please give the lyrics name too !")
        return

    song = ""
    song = Song.find_song(query)
    if song:
        if song.lyrics:
            reply = song.format()
        else:
            reply = "gagal menemukan lirik lagu yang anda minta, coba dengan nama artis nya juga atau gunakan `.glyrics`"
    else:
        reply = "lirik tidak ditemukan, cobalah cari dengan nama artis nya juga atau gunakan `.glyrics`"

    if len(reply) > 4095:
        with io.BytesIO(str.encode(reply)) as out_file:
            out_file.name = "lyrics.text"
            await client.send_document(
                message.chat.id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=query,
                reply_to_msg_id=message.message_id,
            )
            await lel.delete()
    else:
        await lel.edit(reply)
