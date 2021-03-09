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

import io
import asyncio
import inspect
import os
import time
import sys
import traceback
import aiohttp
import json
from telegraph import Telegraph
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup
)

from datetime import datetime
from pyrogram import Client, filters

from tobrot import (
    MAX_MESSAGE_LENGTH,
    DOWNLOAD_LOCATION
)

from tobrot.helper_funcs.display_progress import progress_for_pyrogram

async def down_load_media_f(client, message):
    user_id = message.from_user.id
    print(user_id)
    mess_age = await message.reply_text("processing...", quote=True)
    if not os.path.isdir(DOWNLOAD_LOCATION):
        os.makedirs(DOWNLOAD_LOCATION)
    if message.reply_to_message is not None:
        start_t = datetime.now()
        download_location = "/app/"
        c_time = time.time()
        the_real_download_location = await client.download_media(
            message=message.reply_to_message,
            file_name=download_location,
            progress=progress_for_pyrogram,
            progress_args=(
                "trying to download", mess_age, c_time
            )
        )
        end_t = datetime.now()
        ms = (end_t - start_t).seconds
        
        LOGGER.info(the_real_download_location)
        sam = os.path.basename(the_real_download_location)
        extension = os.path.splitext(the_real_download_location)[1]
        if extension == ".srt" or extension == ".vtt":
           with open(the_real_download_location) as myfile:
             head = [next(myfile) for x in range(7)]
             with open(u_output) as myfile:
               telegraph = Telegraph()
               telegraph.create_account(short_name='1337')
               response = telegraph.create_page(
                 'Subtitle Content',
                 html_content="".join([next(myfile) + "<br>" for x in range(50)])
                    )
               file_context= 'https://telegra.ph/{}'.format(response['path'])
             await mess_age.edit_text(f"<b>OUTPUT:</b>\n\n<code>{the_real_download_location}</code>\n\n<b>First 7 lines of Sub:</b>\n\n<code>{head}</code>\n\nFinished in <u>{ms}</u> seconds",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('🌿 Subtitle Content 🌿', url=file_context)],]))
             the_real_download_location_g = os.path.basename(the_real_download_location)
             LOGGER.info(the_real_download_location_g)
        else:
           await mess_age.edit_text(f"<b>OUTPUT:</b>\n\n<code>{the_real_download_location}</code>\n\nFinished in <u>{ms}</u> seconds")
           the_real_download_location_g = os.path.basename(the_real_download_location)
           LOGGER.info(the_real_download_location_g)

    else:
        #await asyncio.sleep(4)
        await mess_age.edit_text("Reply to a Telegram Media, to save to the server.")
