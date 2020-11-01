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
    MAX_MESSAGE_LENGTH
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
       reply_to_id = message.message_id
       if message.reply_to_message:
         reply_to_id = message.reply_to_message.message_id
       try:
         a , b , c= message.text.split("|")
         file = a.split(" ")[1]
         sub = b.split(" ")[1]
         output = c.split(" ")[1]
         mcover="/app/cover.jpg"
         e , o = await run_command(["ffmpeg", "-i", file, "-i", sub, "-c", "copy", "-c:s", "srt", "-attach", mcover, "-metadata:s:t", "mimetype=image/jpeg", "-metadata:s:t", "filename=cover.jpg", "-metadata", "title=Upl'd By Team-D&O @dramaost TG Group", output])
         if not e:
           e = "No Error"
           o = stdout.decode()
         if not o:
           o = "No Output"
         else:
           _o = o.split("\n")
           o = "\n".join(_o)
         OUTPUT = f"**QUERY:**\n__Command:__\n\n**stderr:** \n{e}`\n**Output:**\n{o}"

         if len(OUTPUT) > MAX_MESSAGE_LENGTH:
           with open("exec.text", "w+", encoding="utf8") as out_file:
               out_file.write(str(OUTPUT))
           user_id = message.from_user.id
           mention_req_user = f"<a href='tg://user?id={user_id}'>{output}</a>\n\n"
           await client.send_document(
                chat_id=message.chat.id,
                document="exec.text",
                caption= mention_req_user,
                disable_notification=True,
                reply_to_message_id=reply_to_id
             )
           os.remove("exec.text")
           await status_message.delete()
         else:
           await status_message.edit(OUTPUT)  
       except IndexError:
         pass
         await status_message.edit("please type output name with run command")
    
async def domux_f(client, message):
       status_message = await message.reply_text("Processing ...")
       reply_to_id = message.message_id
       if message.reply_to_message:
          reply_to_id = message.reply_to_message.message_id
       try:
         a , b, c= message.text.split("|")
         file = a.split(" ")[1]
         sub = b.split(" ")[1]
         output = c.split(" ")[1]
         mcover="/app/Docover.jpg"
         e , o = await run_command(["ffmpeg", "-i", file, "-i", sub, "-c", "copy", "-c:s", "srt", "-attach", mcover, "-metadata:s:t", "mimetype=image/jpeg", "-metadata:s:t", "filename=cover.jpg", "-metadata", "title=Upl'd By Team-D&O @dramaost TG Group", output])
         if not e:
           e = "No Error"
           o = stdout.decode()
         if not o:
           o = "No Output"
         else:
           _o = o.split("\n")
           o = "\n".join(_o)
         OUTPUT = f"**QUERY:**\n__Command:__\n\n**stderr:** \n{e}`\n**Output:**\n{o}"

         if len(OUTPUT) > MAX_MESSAGE_LENGTH:
           with open("exec.text", "w+", encoding="utf8") as out_file:
               out_file.write(str(OUTPUT))
           user_id = message.from_user.id
           mention_req_user = f"<a href='tg://user?id={user_id}'>{output}</a>\n\n"
           await client.send_document(
                chat_id=message.chat.id,
                document="exec.text",
                caption= mention_req_user,
                disable_notification=True,
                reply_to_message_id=reply_to_id
             )
           os.remove("exec.text")
           await status_message.delete()
         else:
           await status_message.edit(OUTPUT)  
       except IndexError:
         pass
         await status_message.edit("please type output name with run command")
 
async def remux_f(client, message):
       status_message = await message.reply_text("Processing ...")
       reply_to_id = message.message_id
       if message.reply_to_message:
         reply_to_id = message.reply_to_message.message_id
       try:
         a , c= message.text.split("|")
         file = a.split(" ")[1]
         output = c.split(" ")[1]
         mcover="/app/cover.jpg"
         e , o = await run_command(["ffmpeg", "-i", file, "-c", "copy", "-attach", mcover, "-metadata:s:t", "mimetype=image/jpeg", "-metadata:s:t", "filename=cover.jpg", "-metadata", "title=Upl'd By Team-D&O @dramaost TG Group", output])
         if not e:
           e = "No Error"
           o = stdout.decode()
         if not o:
           o = "No Output"
         else:
           _o = o.split("\n")
           o = "\n".join(_o)
         OUTPUT = f"**QUERY:**\n__Command:__\n\n**stderr:** \n{e}`\n**Output:**\n{o}"

         if len(OUTPUT) > MAX_MESSAGE_LENGTH:
           with open("exec.text", "w+", encoding="utf8") as out_file:
               out_file.write(str(OUTPUT))
           user_id = message.from_user.id
           mention_req_user = f"<a href='tg://user?id={user_id}'>{output}</a>\n\n"
           await client.send_document(
                chat_id=message.chat.id,
                document="exec.text",
                caption= mention_req_user,
                disable_notification=True,
                reply_to_message_id=reply_to_id
             )
           os.remove("exec.text")
           await status_message.delete()
         else:
           await status_message.edit(OUTPUT)  
       except IndexError:
         pass
         await status_message.edit("please type output name with run command")
    
async def automux_f(client, message):
    status_message = await message.reply_text("Processing ...")
    reply_to_id = message.message_id
    if message.reply_to_message:
      reply_to_id = message.reply_to_message.message_id
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
       try:
         output = message.text.split(" ")[1]
         mcover="/app/Docover.jpg"
         e , o = await run_command(["ffmpeg", "-i", file, "-i", sub, "-c", "copy", "-c:s", "srt", "-attach", mcover, "-metadata:s:t", "mimetype=image/jpeg", "-metadata:s:t", "filename=cover.jpg", "-metadata", "title=Upl'd & Enc'd By Team-D&O @dramaost TG Group", output])
         if not e:
           e = "No Error"
           o = stdout.decode()
         if not o:
           o = "No Output"
         else:
           _o = o.split("\n")
           o = "\n".join(_o)
         OUTPUT = f"**QUERY:**\n__Command:__\n\n**stderr:** \n{e}`\n**Output:**\n{o}"

         if len(OUTPUT) > MAX_MESSAGE_LENGTH:
           with open("exec.text", "w+", encoding="utf8") as out_file:
               out_file.write(str(OUTPUT))
           user_id = message.from_user.id
           mention_req_user = f"<a href='tg://user?id={user_id}'>{output}</a>\n\n"
           await client.send_document(
                chat_id=message.chat.id,
                document="exec.text",
                caption= mention_req_user,
                disable_notification=True,
                reply_to_message_id=reply_to_id
             )
           os.remove("exec.text")
           await status_message.delete()
         else:
           await status_message.edit(OUTPUT)  
       except IndexError:
         pass
         await status_message.edit("please type output name with run command")
    
async def autosubmux_f(client, message):
       status_message = await message.reply_text("Processing ...")
       reply_to_id = message.message_id
       if message.reply_to_message:
         reply_to_id = message.reply_to_message.message_id
       w=message.reply_to_message.message_id
       user_id = message.chat.id
       u_id = int(w)
       m = await client.get_messages(user_id, u_id)
       if m and m.document and m.document.file_name.lower().endswith(".srt"):
         sub = await m.download("/app/")
    #  
       try:
         a , c= message.text.split("|")
         file = a.split(" ")[1]
         output = c.split(" ")[1]
         mcover="/app/Docover.jpg"
         e , o = await run_command(["ffmpeg", "-i", file, "-i", sub, "-c", "copy", "-c:s", "srt", "-attach", mcover, "-metadata:s:t", "mimetype=image/jpeg", "-metadata:s:t", "filename=cover.jpg", "-metadata", "title=Upl'd & Enc'd By Team-D&O @dramaost TG Group", output])
         if not e:
           e = "No Error"
           o = stdout.decode()
         if not o:
           o = "No Output"
         else:
           _o = o.split("\n")
           o = "\n".join(_o)
         OUTPUT = f"**QUERY:**\n__Command:__\n\n**stderr:** \n{e}`\n**Output:**\n{o}"

         if len(OUTPUT) > MAX_MESSAGE_LENGTH:
           with open("exec.text", "w+", encoding="utf8") as out_file:
               out_file.write(str(OUTPUT))
           user_id = message.from_user.id
           mention_req_user = f"<a href='tg://user?id={user_id}'>{output}</a>\n\n"
           await client.send_document(
                chat_id=message.chat.id,
                document="exec.text",
                caption= mention_req_user,
                disable_notification=True,
                reply_to_message_id=reply_to_id
             )
           os.remove("exec.text")
           await status_message.delete()
         else:
           await status_message.edit(OUTPUT)  
       except IndexError:
         pass
         await status_message.edit("please type output name with run command")
    
async def muxget_f(client, message):
    status_message = await message.reply_text("Processing ...")
    w=message.reply_to_message.message_id
    reply_to_id = message.message_id
    if message.reply_to_message:
      reply_to_id = message.reply_to_message.message_id
    user_id = message.chat.id
    u_id = int(w)
    m = await client.get_messages(user_id, u_id)
    if m and m.text and m.text.lower().startswith("https:"):
       link_text = m.text
       try:
         u_output= message.text.split(" ", 1)[1].rsplit(" ", 0)[0]
         e , o = await run_command(["wget", "-c", link_text, "-O", u_output])
         if not e:
           e = "No Error"
           o = stdout.decode()
         if not o:
           o = "No Output"
         else:
           _o = o.split("\n")
           o = "\n".join(_o)
         OUTPUT = f"**QUERY:**\n__Command:__\n\n**stderr:** \n{e}`\n**Output:**\n{o}"

         if len(OUTPUT) > MAX_MESSAGE_LENGTH:
           with open("exec.text", "w+", encoding="utf8") as out_file:
               out_file.write(str(OUTPUT))
           user_id = message.from_user.id
           mention_req_user = f"<a href='tg://user?id={user_id}'>{u_output}</a>\n\n"
           await client.send_document(
                chat_id=message.chat.id,
                document="exec.text",
                caption= mention_req_user,
                disable_notification=True,
                reply_to_message_id=reply_to_id
             )
           os.remove("exec.text")
           await status_message.delete()
         else:
           await status_message.edit(OUTPUT)  
       except IndexError:
         pass
         await status_message.edit("please type output name with run command")
    #
    await status_message.edit("Replied Text is not link")    
    
async def muxyou_f(client, message):
    status_message = await message.reply_text("Processing ...")
    w=message.reply_to_message.message_id
    reply_to_id = message.message_id
    if message.reply_to_message:
      reply_to_id = message.reply_to_message.message_id
    user_id = message.chat.id
    u_id = int(w)
    m = await client.get_messages(user_id, u_id)
    if m and m.text and m.text.lower().startswith("https:"):
       link_text = m.text
       try:
          u_output= message.text.split(" ", 1)[1].rsplit(" ", 0)[0]
          e , o = await run_command(["youtube-dl", "-o", u_output, link_text])
          if not e:
            e = "No Error"
            o = stdout.decode()
          if not o:
            o = "No Output"
          else:
            _o = o.split("\n")
            o = "\n".join(_o)
          OUTPUT = f"**QUERY:**\n__Command:__\n\n**stderr:** \n{e}`\n**Output:**\n{o}"

          if len(OUTPUT) > MAX_MESSAGE_LENGTH:
            with open("exec.text", "w+", encoding="utf8") as out_file:
                out_file.write(str(OUTPUT))
            user_id = message.from_user.id
            mention_req_user = f"<a href='tg://user?id={user_id}'>{u_output}</a>\n\n"
            await client.send_document(
                chat_id=message.chat.id,
                document="exec.text",
                caption= mention_req_user,
                disable_notification=True,
                reply_to_message_id=reply_to_id
              )
            os.remove("exec.text")
            await status_message.delete()
          else:
            await status_message.edit(OUTPUT)  
       except IndexError:
          pass
          await status_message.edit("please type output name with run command")
    #
    await status_message.edit("Replied Text is not link") 


async def gdfile_f(client, message):
    status_message = await message.reply_text("Processing ...")
    w=message.reply_to_message.message_id
    reply_to_id = message.message_id
    if message.reply_to_message:
      reply_to_id = message.reply_to_message.message_id
    user_id = message.chat.id
    u_id = int(w)
    m = await client.get_messages(user_id, u_id)
    if m and m.text and m.text.lower().startswith("https:"):
       link_text = m.text
       try:
          u_output = message.text.split(" ", 1)[1].rsplit(" ", 0)[0]
          await run_command(["chmod", "a+x", "./gdown.pl"])
          e , o = await run_command(["./gdown.pl", link_text, u_output])
          if not e:
            e = "No Error"
            o = stdout.decode()
          if not o:
            o = "No Output"
          else:
            _o = o.split("\n")
            o = "\n".join(_o)
          OUTPUT = f"**QUERY:**\n__Command:__\n\n**stderr:** \n{e}`\n**Output:**\n{o}"

          if len(OUTPUT) > MAX_MESSAGE_LENGTH:
            with open("exec.text", "w+", encoding="utf8") as out_file:
                out_file.write(str(OUTPUT))
            user_id = message.from_user.id
            mention_req_user = f"<a href='tg://user?id={user_id}'>{u_output}</a>\n\n"
            await client.send_document(
                chat_id=message.chat.id,
                document="exec.text",
                caption= mention_req_user,
                disable_notification=True,
                reply_to_message_id=reply_to_id
              )
            os.remove("exec.text")
            await status_message.delete()
          else:
            await status_message.edit(OUTPUT)  
       except IndexError:
          pass
          await status_message.edit("please type output name with run command")
    #
    await status_message.edit("Replied Text is not link")
    
