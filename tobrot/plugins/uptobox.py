import json
import os
import shutil
import time
from pyrogram import filters
from pyrogram.types import (
    Message
)
from tobrot import (
    LOGGER,
    AUTH_USERS,
    UPTO_BOX_TOKEN,
    TG_MAX_FILE_SIZE,
    DOWNLOAD_LOCATION
)
from bot.bot import Bot
from bot.helpers.link_fliter import _link_match_filt_er
from tobrot.helper_funcs.display_progress import (
    humanbytes,
    progress_for_pyrogram
)
from bot.helpers.run_shell_command import run_command
from bot.helpers.uptobox.get_file_info import upto_box_get_file_info
from bot.helpers.uptobox.get_leech_file_link import (
    upto_box_get_file_link
)

async def leech_upto_box_fn(client,message):
    status_message = await message.reply_text(
        "Processing...",
        quote=True
    )
    download_location = os.path.join(
        DOWNLOAD_LOCATION,
        str(status_message.message_id)
    )
    if not os.path.isdir(download_location):
        os.makedirs(download_location)
    upto_box_url = message.leech_url
    upto_box_id = upto_box_url.split("/")[-1]
    file_infos = await upto_box_get_file_info(upto_box_id)
    # LOGGER(__name__).info(file_infos)
    if file_infos.get("statusCode") == 0:
        file_list = file_infos.get("data").get("list")
        for one_file in file_list:
            file_code = one_file.get("file_code")
            file_size = one_file.get("file_size")
            real_file_name = one_file.get("file_name")
            if not file_size:
                await message.reply_text(
                    json.dumps(one_file.get("error"), indent=4),
                    quote=True
                )
                continue
            if file_size < TG_MAX_FILE_SIZE:
                leech_file_links = await upto_box_get_file_link(
                    UPTO_BOX_TOKEN,
                    file_code
                )
                # LOGGER(__name__).info(leech_file_links)
                custom_file_name = message.custom_file_name
                if not custom_file_name:
                    custom_file_name = real_file_name
                if leech_file_links.get("statusCode") == 0:
                    dlLink = leech_file_links.get("data").get("dlLink")
                    current_file_apht = os.path.join(
                        download_location,
                        custom_file_name
                    )
                    await run_command([
                        "wget",
                        "-c",
                        dlLink,
                        "-O",
                        current_file_apht
                    ])
                    if os.path.isfile(current_file_apht):
                        start_time = time.time()
                        await message.reply_document(
                            current_file_apht,
                            quote=True,
                            thumb=None,
                            caption=(
                                f"<b>URL</b>: {upto_box_url}\n"
                                f"<b>File Name</b>: <code>{real_file_name}</code>\n\n"
                                "Subscribe <a href='"
                                "https://t.me/kdramaupdates/16636'>"
                                "@dramaOST"
                                "</a>"
                            ),
                            progress=progress_for_pyrogram,
                            progress_args=(
                                (
                                    "Daily Updates Channel "
                                    "for @dramaost Group ...\n"
                                ),
                                status_message,
                                start_time
                            )
                        )
                        os.remove(current_file_apht)
                else:
                    await status_message.reply_text(
                        leech_file_links.get("data"),
                        quote=True
                    )
            else:
                await status_message.reply_text(
                    (
                        f"<code>{real_file_name}</code> "
                        "is "
                        f"<code>{humanbytes(file_size)}</code>"
                        " > "
                        f"<b>{humanbytes(TG_MAX_FILE_SIZE)}</b>"
                    ),
                    quote=True
                )
    else:
        await status_message.reply_text(
            file_infos.get("data"),
            quote=True
        )
    shutil.rmtree(download_location, ignore_errors=True)
    await status_message.delete()
