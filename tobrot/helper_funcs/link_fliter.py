from pyrogram import filters


def _link_match_filt_er(link_kw: str):
    def func(flt, client, message):
        if message and message.text:
            if flt.wok in message.text:
                leech_url = None
                custom_file_name = None
                for one_entity in message.entities:
                    if one_entity.type == "url":
                        leech_url = message.text[
                            one_entity.offset:one_entity.offset + one_entity.length
                        ]
                    elif one_entity.type == "text_link":
                        leech_url = one_entity.url
                    if leech_url and flt.wok in leech_url:
                        break
                if "|" in message.text:
                    _, custom_file_name = message.text.split("|")
                if leech_url:
                    message.leech_url = leech_url.strip()
                if custom_file_name:
                    message.custom_file_name = custom_file_name.strip()
                else:
                    message.custom_file_name = None
                return True
        return False
    # wok kwarg is accessed with flt.wok above
    return filters.create(func, wok=link_kw)
