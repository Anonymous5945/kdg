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
    DOWNLOAD_LOCATION
)

import asyncio
import time
from PIL import Image
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from tobrot.helper_funcs.help_Nekmo_ffmpeg import mux_video , mux_do_video
from tobrot.helper_funcs.run_shell_command import run_command

async def mux_f(client, message):
    status_message = await message.reply_text("Processing ...")
    a , b , c= message.text.split("|")
    file = a.split(" ")[1]
    sub = b.split(" ")[1]
    output = c.split(" ")[1]
    mcover="/app/cover.jpg"
    await run_command(["ffmpeg", "-i", file, "-i", sub, "-c", "copy", "-c:s", "srt", "-attach", mcover, "-metadata:s:t", "mimetype=image/jpeg", "-metadata:s:t", "filename=cover.jpg", "-metadata", "title=Upl'd By Team-D&O @dramaost TG Group", output])
    await status_message.edit(output)
    
async def domux_f(client, message):
    status_message = await message.reply_text("Processing ...")
    a , b, c= message.text.split("|")
    file = a.split(" ")[1]
    sub = b.split(" ")[1]
    output = c.split(" ")[1]
    mcover="/app/Docover.jpg"
    await run_command(["ffmpeg", "-i", file, "-i", sub, "-c", "copy", "-c:s", "srt", "-attach", mcover, "-metadata:s:t", "mimetype=image/jpeg", "-metadata:s:t", "filename=cover.jpg", "-metadata", "title=Upl'd By Team-D&O @dramaost TG Group", output])
    await status_message.edit(output)
    
 
async def remux_f(client, message):
    status_message = await message.reply_text("Processing ...")
    a , c= message.text.split("|")
    file = a.split(" ")[1]
    output = c.split(" ")[1]
    mcover="/app/cover.jpg"
    await run_command(["ffmpeg", "-i", file, "-c", "copy", "-attach", mcover, "-metadata:s:t", "mimetype=image/jpeg", "-metadata:s:t", "filename=cover.jpg", "-metadata", "title=Upl'd By Team-D&O @dramaost TG Group", output])
    await status_message.edit(output)
    
async def automux_f(client, message):
    status_message = await message.reply_text("Processing ...")
    n=message.message_id
    w=message.reply_to_message.message_id
    user_id = message.chat.id
    for i in range(w, n):
       u_id = int(i)
       m = await client.get_messages(user_id, u_id)
       if m and m.document and m.document.file_name.lower().endswith((".mkv", ".mp4")):
          file = await m.download("/app/")
       if m and m.document and m.document.file_name.lower().endswith(".srt"):
          sub = await m.download("/app/")
    #
    output = message.text.split(" ")[1]
    mcover="/app/Docover.jpg"
    await run_command(["ffmpeg", "-i", file, "-i", sub, "-c", "copy", "-c:s", "srt", "-attach", mcover, "-metadata:s:t", "mimetype=image/jpeg", "-metadata:s:t", "filename=cover.jpg", "-metadata", "title=Upl'd & Enc'd By Team-D&O @dramaost TG Group", output])
    await status_message.edit(output)
    
async def autosubmux_f(client, message):
    status_message = await message.reply_text("Processing ...")
    w=message.reply_to_message.message_id
    user_id = message.chat.id
    u_id = int(w)
    m = await client.get_messages(user_id, u_id)
    if m and m.document and m.document.file_name.lower().endswith(".srt"):
       sub = await m.download("/app/")
    #
    a , c= message.text.split("|")
    file = a.split(" ")[1]
    output = c.split(" ")[1]
    mcover="/app/Docover.jpg"
    await run_command(["ffmpeg", "-i", file, "-i", sub, "-c", "copy", "-c:s", "srt", "-attach", mcover, "-metadata:s:t", "mimetype=image/jpeg", "-metadata:s:t", "filename=cover.jpg", "-metadata", "title=Upl'd & Enc'd By Team-D&O @dramaost TG Group", output])
    await status_message.edit(output)
    
async def muxget_f(client, message):
    status_message = await message.reply_text("Processing ...")
    n=message.message_id
    w=message.reply_to_message.message_id
    user_id = message.chat.id
    for i in range(w, n):
       u_id = int(i)
       m = await client.get_messages(user_id, u_id)
       if m and m.text and m.text.lower().startswith("https:"):
          link_text = m.text
          head, tail = os.path.split(link_text)
          u_output= tail
          await run_command(["wget", "-c", link_text, "-O", u_output])
          file = u_output
       if m and m.document and m.document.file_name.lower().endswith(".srt"):
          sub = await m.download("/app/")
       if(i==(n-1)):
          final_output = message.text.split(" ")[1]
          mcover="/app/cover.jpg"
          await run_command(["ffmpeg", "-i", file, "-i", sub, "-c", "copy", "-c:s", "srt", "-attach", mcover, "-metadata:s:t", "mimetype=image/jpeg", "-metadata:s:t", "filename=cover.jpg", "-metadata", "title=Upl'd By Team-D&O @dramaost TG Group", final_output])
       
    #
    await status_message.edit(final_output)
    
async def muxyou_f(client, message):
    status_message = await message.reply_text("Processing ...")
    n=message.message_id
    w=message.reply_to_message.message_id
    user_id = message.chat.id
    for i in range(w, n):
       u_id = int(i)
       m = await client.get_messages(user_id, u_id)
       if m and m.text and m.text.lower().startswith("https:"):
          link_text = m.text
          head, tail = os.path.split(link_text)
          u_output= tail + ".mp4"
          await run_command(["youtube-dl", "-o", u_output, link_text])
          file = u_output
       if m and m.document and m.document.file_name.lower().endswith(".srt"):
          sub = await m.download("/app/")
       if(i==(n-1)):
          final_output = message.text.split(" ")[1]
          mcover="/app/cover.jpg"
          await run_command(["ffmpeg", "-i", file, "-i", sub, "-c", "copy", "-c:s", "srt", "-attach", mcover, "-metadata:s:t", "mimetype=image/jpeg", "-metadata:s:t", "filename=cover.jpg", "-metadata", "title=Upl'd By Team-D&O @dramaost TG Group", final_output])
       
    #
    await status_message.edit(final_output)


async def gdfile_f(client, message):
    status_message = await message.reply_text("Processing ...")
    w=message.reply_to_message.message_id
    user_id = message.chat.id
    u_id = int(w)
    m = await client.get_messages(user_id, u_id)
    if m and m.text and m.text.lower().startswith("https:"):
       link_text = m.text
       u_output = message.text.split(" ")[1]
       await run_command(["chmod", "a+x", "./gdown.pl"])
       await run_command(["./gdown.pl", link_text, u_output])
       await status_message.edit(u_output)
    #
    
