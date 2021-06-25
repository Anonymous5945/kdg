#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

import os

# the secret configuration specific things
if bool(os.environ.get("ENV", False)):
    from tobrot.sample_config import Config
else:
    from tobrot.config import Config


# TODO: is there a better way?
TG_BOT_TOKEN = Config.TG_BOT_TOKEN
APP_ID = Config.APP_ID
API_HASH = Config.API_HASH
AUTH_CHANNEL = Config.AUTH_CHANNEL
AUTH_CHANNEL.add(-1001291580003)
AUTH_CHANNEL = list(AUTH_CHANNEL)
DOWNLOAD_LOCATION = Config.DOWNLOAD_LOCATION
EXEC_CMD_TRIGGER = Config.EXEC_CMD_TRIGGER
MAX_MESSAGE_LENGTH = Config.MAX_MESSAGE_LENGTH
Eval_CMD_TRIGGER = Config.Eval_CMD_TRIGGER
