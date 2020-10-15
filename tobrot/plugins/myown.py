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
    await run_command(["ffmpeg", "-i", file, "-i", sub, "-c", "copy", "-attach", mcover, "-metadata:s:t", "mimetype=image/jpeg", "-metadata:s:t", "filename=cover.jpg", "-metadata", "title=Upl'd By Team-D&O @dramaost TG Group", output])
    await status_message.edit(output)
    
async def mux_do_f(client, message):
    status_message = await message.reply_text("Processing ...")
    a , b, c= message.text.split("|")
    file = a.split(" ")[1]
    sub = b.split(" ")[1]
    output = c.split(" ")[1]
    mcover="/app/Docover.jpg"
    await run_command(["ffmpeg", "-i", file, "-i", sub, "-c", "copy", "-attach", mcover, "-metadata:s:t", "mimetype=image/jpeg", "-metadata:s:t", "filename=cover.jpg", "-metadata", "title=Upl'd By Team-D&O @dramaost TG Group", output])
    await status_message.edit(output)
    
 
async def remux_f(client, message):
    status_message = await message.reply_text("Processing ...")
    a , c= message.text.split("|")
    file = a.split(" ")[1]
    output = c.split(" ")[1]
    mcover="/app/Docover.jpg"
    await run_command(["ffmpeg", "-i", file, "-c", "copy", "-attach", mcover, "-metadata:s:t", "mimetype=image/jpeg", "-metadata:s:t", "filename=cover.jpg", "-metadata", "title=Upl'd & Enc'd By Team-D&O @dramaost TG Group", output])
    await status_message.edit(output)
   
