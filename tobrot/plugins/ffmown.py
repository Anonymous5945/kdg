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
import shlex,subprocess
from PIL import Image
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser

async def multi_f(client, message):
       status_message = await message.reply_text("Processing ...")
       reply_to_id = message.message_id
       if message.reply_to_message:
         reply_to_id = message.reply_to_message.message_id
       try:
         a,file,sub,name=shlex.split(message.text)
         out ="@dramaOST." + name + ".mkv"
         h = os.listdir(sub)
         nom = len(h) + 1
         h.sort()
         n=0
         w=1
         sam = 'ffmpeg' + ' -i ' + '"'+ file + '" ' + " ".join(['-i ' + '"' + sub + "/" + j + '" ' for j in h]) + ' ' +  '-map ' +  '0:0 ' + '-map ' +  '0:1 ' + " ".join(['-map ' + str(j) + ' ' for j in range(w,nom)]) + " ".join(['-metadata:s:s:' +str(i) + ' ' + 'language='+ j[:3] + ' ' for i,j in zip(range(n,nom) , h)]) + '-c ' + 'copy ' + '-c:s ' + 'srt ' + '-attach ' + '/app/Docover.jpg ' + '-metadata:s:t ' + 'mimetype=image/jpeg ' + '-metadata:s:t ' + 'filename=cover.jpg ' + '-metadata ' + 'title="Upl.ed By Team-D&O @dramaost TG Group" ' + '"' + out + '"'
         Goh = shlex.split(sam)
         process = await asyncio.create_subprocess_exec(
                 *Goh,
                 stdout=asyncio.subprocess.PIPE,
                 stderr=asyncio.subprocess.PIPE,
             )
         stdout, stderr = await process.communicate()
         e_response = stderr.decode().strip()
         t_response = stdout.decode().strip()
         e = e_response
         if not e:
           e = "No Error"
         o = t_response
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
           mention_req_user = f"<a href='tg://user?id={user_id}'>{out}</a>\n\n"
           await message.reply_document(
                document="exec.text",
                caption= mention_req_user,
                disable_notification=True
             )
           os.remove("exec.text")
           await status_message.delete()
         else:
           await status_message.edit(OUTPUT)  
       except IndexError:
         pass
         await status_message.edit("please type output name with run command")
  
