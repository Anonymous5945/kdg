import os

class Config(object):
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
    # The Telegram API things
    APP_ID = int(os.environ.get("APP_ID", 12345))
    API_HASH = os.environ.get("API_HASH")
    # Get these values from my.telegram.org
    # to store the channel ID who are authorized to use the bot
    user_ids1 = set(int(x) for x in os.environ.get("user_ids1", "").split())
    user_ids2 = set(int(x) for x in os.environ.get("user_ids2", "").split())
    AUTH_CHANNEL = set(int(x) for x in os.environ.get("AUTH_CHANNEL", "").split())
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # EXEC command trigger
    EXEC_CMD_TRIGGER = os.environ.get("EXEC_CMD_TRIGGER", "exec")
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    #
    EDIT_SLEEP_TIME_OUT = int(os.environ.get("EDIT_SLEEP_TIME_OUT", 4))
    MAX_TG_SPLIT_FILE_SIZE = int(os.environ.get("MAX_TG_SPLIT_FILE_SIZE", 1072864000))
    # ytdl command
    Ytdl_CMD_TRIGGER = os.environ.get("Ytdl_CMD_TRIGGER", "ytdl")
    # Eval command
    Eval_CMD_TRIGGER = os.environ.get("Eval_CMD_TRIGGER", "eval")
    # upload command
    Upload_CMD_TRIGGER = os.environ.get("Upload_CMD_TRIGGER", "upload")
    # savethumbnail command
    Save_Thumb_CMD_TRIGGER = os.environ.get("Save_Thumb_CMD_TRIGGER", "save")
    # clear thumbnail command
    Clear_thumb_CMD_TRIGGER = os.environ.get("Clear_thumb_CMD_TRIGGER", "clear")
    TELEGRAM_CMD_TRIGGER = os.environ.get("TELEGRAM_CMD_TRIGGER", "down")
    # add offensive API
    TG_OFFENSIVE_API = os.environ.get("TG_OFFENSIVE_API", None)
    Mass_CMD_TRIGGER = os.environ.get("Mass_CMD_TRIGGER", "mass")
    kdg1_CMD_TRIGGER = os.environ.get("kdg1_CMD_TRIGGER", "kdg1")
    kdg2_CMD_TRIGGER = os.environ.get("kdg2_CMD_TRIGGER", "kdg2")
    Youmux_CMD_TRIGGER = os.environ.get("Youmux_CMD_TRIGGER", "you")
    Getmux_CMD_TRIGGER = os.environ.get("Getmux_CMD_TRIGGER", "get")
    Gd_CMD_TRIGGER = os.environ.get("Gd_CMD_TRIGGER", "gd")
    Fir_CMD_TRIGGER = os.environ.get("Fir_CMD_TRIGGER", "")
