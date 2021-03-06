import os

class Config(object):
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
    # The Telegram API things
    APP_ID = int(os.environ.get("APP_ID", 12345))
    API_HASH = os.environ.get("API_HASH")
    AUTH_CHANNEL = set(int(x) for x in os.environ.get("AUTH_CHANNEL", "").split())
    # the download location
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # EXEC command trigger
    EXEC_CMD_TRIGGER = os.environ.get("EXEC_CMD_TRIGGER", "exec")
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # Eval command
    Eval_CMD_TRIGGER = os.environ.get("Eval_CMD_TRIGGER", "eval")
   
