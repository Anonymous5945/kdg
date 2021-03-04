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
user_ids1 = Config.user_ids1
user_ids1 = list(user_ids1)
user_ids2 = Config.user_ids2
user_ids2 = list(user_ids2)
DOWNLOAD_LOCATION = Config.DOWNLOAD_LOCATION
EXEC_CMD_TRIGGER = Config.Fir_CMD_TRIGGER + Config.EXEC_CMD_TRIGGER
MAX_FILE_SIZE = Config.MAX_FILE_SIZE
TG_MAX_FILE_SIZE = Config.TG_MAX_FILE_SIZE
FREE_USER_MAX_FILE_SIZE = Config.FREE_USER_MAX_FILE_SIZE
CHUNK_SIZE = Config.CHUNK_SIZE
DEF_THUMB_NAIL_VID_S = Config.DEF_THUMB_NAIL_VID_S
MAX_MESSAGE_LENGTH = Config.MAX_MESSAGE_LENGTH
PROCESS_MAX_TIMEOUT = Config.PROCESS_MAX_TIMEOUT
EDIT_SLEEP_TIME_OUT = Config.EDIT_SLEEP_TIME_OUT
MAX_TG_SPLIT_FILE_SIZE = Config.MAX_TG_SPLIT_FILE_SIZE
PROCESS_RUNNING = "processing ..."
Ytdl_CMD_TRIGGER = Config.Fir_CMD_TRIGGER + Config.Ytdl_CMD_TRIGGER
Eval_CMD_TRIGGER = Config.Fir_CMD_TRIGGER + Config.Eval_CMD_TRIGGER
Upload_CMD_TRIGGER = Config.Fir_CMD_TRIGGER + Config.Upload_CMD_TRIGGER
Save_Thumb_CMD_TRIGGER = Config.Fir_CMD_TRIGGER + Config.Save_Thumb_CMD_TRIGGER
Clear_thumb_CMD_TRIGGER = Config.Fir_CMD_TRIGGER + Config.Clear_thumb_CMD_TRIGGER
TELEGRAM_CMD_TRIGGER = Config.Fir_CMD_TRIGGER + Config.TELEGRAM_CMD_TRIGGER
TG_OFFENSIVE_API = Config.TG_OFFENSIVE_API
Mass_CMD_TRIGGER = Config.Fir_CMD_TRIGGER + Config.Mass_CMD_TRIGGER
kdg1_CMD_TRIGGER = Config.Fir_CMD_TRIGGER + Config.kdg1_CMD_TRIGGER
kdg2_CMD_TRIGGER = Config.Fir_CMD_TRIGGER + Config.kdg2_CMD_TRIGGER
Youmux_CMD_TRIGGER = Config.Fir_CMD_TRIGGER + Config.Youmux_CMD_TRIGGER
Getmux_CMD_TRIGGER = Config.Fir_CMD_TRIGGER + Config.Getmux_CMD_TRIGGER
Gd_CMD_TRIGGER = Config.Fir_CMD_TRIGGER + Config.Gd_CMD_TRIGGER
