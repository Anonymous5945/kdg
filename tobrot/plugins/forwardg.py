#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)


import os

from tobrot import (
    DOWNLOAD_LOCATION,
    MAX_MESSAGE_LENGTH,
    user_ids1,
    user_ids2
)

import asyncio
import time
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup
)

async def kdg1_f(client, message):
    status_message = await message.reply_text("Processing ...")
    n=message.message_id
    w=message.reply_to_message.message_id
    user_id = message.chat.id
    user_id = message.chat.id
    for i in range(w, n):
     u_id = int(i)
     m = await client.get_messages(user_id, u_id)
     for user in user_ids1:
      if m.text:
       await client.forward_messages(
       chat_id=user,
       from_chat_id=message.chat.id,
       message_ids = u_id,
       as_copy=True
       )
       await asyncio.sleep(3)
      if m.media and m.document and m.document.file_name.lower().endswith(".mp4"):
        await client.send_document(user,m.document.file_id, caption= "<b>" + m.document.file_name + "</b>" + "\n\n" +"<b>@kdg_166  @korea_drama @kdg166_ongoing @kdgfiles</b>")
        await asyncio.sleep(3)
      if m.media and m.document and m.document.file_name.lower().endswith(".mkv"):
        await client.send_document(user,m.document.file_id, caption= "<b>" + m.document.file_name + "</b>" + "\n\n" +"<b>@kdg_166  @korea_drama @kdg166_ongoing @kdgfiles\n\n</b>" +"<b>Muxed English Subtitle\nPlay it via external player</b>")
        await asyncio.sleep(3)
    await status_message.edit("finish")

async def kdg2_f(client, message):
    status_message = await message.reply_text("Processing ...")
    n=message.message_id
    w=message.reply_to_message.message_id
    user_id = message.chat.id
    user_id = message.chat.id
    for i in range(w, n):
     u_id = int(i)
     m = await client.get_messages(user_id, u_id)
     for user in user_ids2:
      if m.text:
       await client.forward_messages(
       chat_id=user,
       from_chat_id=message.chat.id,
       message_ids = u_id,
       as_copy=True
       )
       await asyncio.sleep(3)
      if m.media and m.document and m.document.file_name.lower().endswith(".mp4"):
        await client.send_document(user,m.document.file_id, caption= "<b>" + m.document.file_name + "</b>" + "\n\n" +"<b>@kdg_166  @korea_drama @kdg166_ongoing @kdgfiles</b>")
        await asyncio.sleep(3)
      if m.media and m.document and m.document.file_name.lower().endswith(".mkv"):
        await client.send_document(user,m.document.file_id, caption= "<b>" + m.document.file_name + "</b>" + "\n\n" +"<b>@kdg_166  @korea_drama @kdg166_ongoing @kdgfiles\n\n</b>" +"<b>Muxed English Subtitle\nPlay it via external player</b>")
        await asyncio.sleep(3)
    await status_message.edit("finish")
