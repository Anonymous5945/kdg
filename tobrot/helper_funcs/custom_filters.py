#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from pyrogram import (
    Client,
    filters
)
from pyrogram.types import (
    Message
)


def message_filter_f(flt, c: Client, m: Message):
    return bool(
            (
                # below checks the TORRENT detection part
                m.text and
                m.text.lower().startswith("http") and ("uptobox.com" not in m.text) and (".html" not in m.text)
            ) 
        )


message_fliter = filters.create(
    func=message_filter_f,
    name="TstMesgFilter"
)
