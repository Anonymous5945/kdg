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
from telegraph import Telegraph
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup
)

async def muxget_f(client, message):
       status_message = await message.reply_text("Processing ...")
       try:
        if message.reply_to_message is not None:
         w=message.reply_to_message.message_id
         user_id = message.chat.id
         u_id = int(w)
         m = await client.get_messages(user_id, u_id)
         if m and m.text and m.text.lower().startswith(("https:", "http:")):
          link_text = m.text  
          u_output= message.text.split(" ", 1)[1].rsplit(" ", 0)[0]
          en , on = await run_command(["wget", "-c", link_text, "-O", u_output])
          metadata = extractMetadata(createParser(u_output))
          metadata = extractMetadata(createParser(u_output))
          duration = 0
          if metadata.has("duration"):
            duration = metadata.get('duration').seconds
          hours, rem = divmod(duration, 3600)
          minutes, seconds = divmod(rem, 60)
          Final_duration="{:0>2} hrs {:0>2} min {:05.2f} sec".format(int(hours),int(minutes),seconds)
          telegraph = Telegraph()
          telegraph.create_account(short_name='1337')
          response = telegraph.create_page(
          u_output + ' Media Info',
          html_content="".join(line + "<br>" for line in metadata.exportPlaintext())
          )
          file_context= 'https://telegra.ph/{}'.format(response['path'])
          e = on
          if not e:
            e = "No Error"
          o = en
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
            mention_req_user = f"<a href='tg://user?id={user_id}'>{u_output}</a>"
            await message.reply_document(
                document="exec.text",
                caption= mention_req_user + "\n\n" + "Duration : " + str(duration) + " seconds" + "\n" + "In Standard Time :" + "\n" + Final_duration,
                disable_notification=True,
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('🌿 Media Info 🌿', url=file_context)],])
              )
            os.remove("exec.text")
            await status_message.delete()
          else:
            await status_message.edit(OUTPUT)
         else:
           await status_message.edit("Replied message is not a link")
        else:
           await status_message.edit("Run as Replied message")
       except IndexError:
         pass
         await status_message.edit("please type output name with run command")
       #
   
    
async def muxyou_f(client, message):
       status_message = await message.reply_text("Processing ...")
       try:
        if message.reply_to_message is not None:
         w=message.reply_to_message.message_id
         user_id = message.chat.id
         u_id = int(w)
         m = await client.get_messages(user_id, u_id)
         if m and m.text and m.text.lower().startswith(("https:","http:")):
          link_text = m.text
          u_output= message.text.split(" ", 1)[1].rsplit(" ", 0)[0]
          en , on = await run_command(["youtube-dl", "-o", u_output, link_text])
          metadata = extractMetadata(createParser(u_output))
          metadata = extractMetadata(createParser(u_output))
          duration = 0
          if metadata.has("duration"):
             duration = metadata.get('duration').seconds
          hours, rem = divmod(duration, 3600)
          minutes, seconds = divmod(rem, 60)
          Final_duration="{:0>2} hrs {:0>2} min {:05.2f} sec".format(int(hours),int(minutes),seconds)
          telegraph = Telegraph()
          telegraph.create_account(short_name='1337')
          response = telegraph.create_page(
          u_output + ' Media Info',
          html_content="".join(line + "<br>" for line in metadata.exportPlaintext())
          )
          file_context= 'https://telegra.ph/{}'.format(response['path'])
          e = on
          if not e:
            e = "No Error"
          o = en
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
            mention_req_user = f"<a href='tg://user?id={user_id}'>{u_output}</a>"
            await message.reply_document(
                document="exec.text",
                caption= mention_req_user + "\n\n" + "Duration : " + str(duration) + " seconds" + "\n" + "In Standard Time :" + "\n" + Final_duration,
                disable_notification=True,
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('🌿 Media Info 🌿', url=file_context)],])
              )
            os.remove("exec.text")
            await status_message.delete()
          else:
            await status_message.edit(OUTPUT)  
         else:
           await status_message.edit("Replied message is not a link")
        else:
          await status_message.edit("Run as Replied message")
       except IndexError:
          pass
          await status_message.edit("please type output name with run command")

    #



async def gdfile_f(client, message):
       status_message = await message.reply_text("Processing ...")
       try:
        if message.reply_to_message is not None:
         w=message.reply_to_message.message_id
         user_id = message.chat.id
         u_id = int(w)
         m = await client.get_messages(user_id, u_id)
         if m and m.text and m.text.lower().startswith(("https:","http:")):
          link_text = m.text
          u_output = message.text.split(" ", 1)[1].rsplit(" ", 0)[0]
          await run_command(["chmod", "a+x", "./gdown.pl"])
          en , on = await run_command(["./gdown.pl", link_text, u_output])
          metadata = extractMetadata(createParser(u_output))
          metadata = extractMetadata(createParser(u_output))
          duration = 0
          if metadata.has("duration"):
            duration = metadata.get('duration').seconds
          hours, rem = divmod(duration, 3600)
          minutes, seconds = divmod(rem, 60)
          Final_duration="{:0>2} hrs {:0>2} min {:05.2f} sec".format(int(hours),int(minutes),seconds)
          telegraph = Telegraph()
          telegraph.create_account(short_name='1337')
          response = telegraph.create_page(
          u_output + ' Media Info',
          html_content="".join(line + "<br>" for line in metadata.exportPlaintext())
          )
          file_context= 'https://telegra.ph/{}'.format(response['path'])
          e = on
          if not e:
            e = "No Error"
          o = en
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
            mention_req_user = f"<a href='tg://user?id={user_id}'>{u_output}</a>"
            await message.reply_document(
                document="exec.text",
                caption= mention_req_user + "\n\n" + "Duration : " + str(duration) + " seconds" + "\n" + "In Standard Time :" + "\n" + Final_duration,
                disable_notification=True,
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('🌿 Media Info 🌿', url=file_context)],])
              )
            os.remove("exec.text")
            await status_message.delete()
          else:
            await status_message.edit(OUTPUT)
         else:
           await status_message.edit("Replied message is not a link")
        else:
           await status_message.edit("Run as Replied message")
       except IndexError:
          pass
          await status_message.edit("please type output name with run command")
    #
