import logging
import os
import sys
import time
import telegram.ext as tg
from telethon.sessions import MemorySession
from telethon import TelegramClient
from redis import StrictRedis
from pyrogram import Client, errors

StartTime = time.time()

# enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

LOGGER = logging.getLogger(__name__)

# if version < 3.6, stop bot.
if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    LOGGER.error(
        "You must have a python version of at least 3.6! Multiple features depend on this. Bot quitting."
    )
    quit(1)

ENV = bool(os.environ.get("ENV", False))

if ENV:
    TOKEN = os.environ.get("TOKEN", "5808748296:AAE-mEm_gAqusNZ-C8J9CjQS-yW5uOD-m38")

    try:
        OWNER_ID = int(os.environ.get("OWNER_ID", "2105971379"))
    except ValueError:
        raise Exception("Your OWNER_ID env variable is not a valid integer.")
    try:
        INSPECTOR = {int(x) for x in os.environ.get("INSPECTOR", "6204761408 5705178479").split()}
        DEV_USERS = {int(x) for x in os.environ.get("DEV_USERS", "6204761408 5705178479").split()}
    except ValueError:
        raise Exception(
            "Your inspector(sudo) or dev users list does not contain valid integers.")

    try:
        REQUESTER = {int(x) for x in os.environ.get("REQUESTER", "5360305806 5705178479").split()}
    except ValueError:
        raise Exception("Your requester list does not contain valid integers.")
    try:
        API_ID = int(os.environ.get("API_ID", "12227067"))
    except ValueError:
        raise Exception("Your API_ID env variable is not a valid integer.")

    try:
        API_HASH = os.environ.get("API_HASH", "b463bedd791aa733ae2297e6520302fe")
    except ValueError:
        raise Exception("Please Add Hash Api key to start the bot")

    DB_URI = os.environ.get("DATABASE_URL","postgres://cbtysxae:AxhFIfnAH0KCMVtOwAUE25shztdqb2P9@peanut.db.elephantsql.com/cbtysxae")
    PHOTO = os.environ.get("PHOTO", "https://graph.org/file/2d3f35226a0d59cbb9980.jpg") # Miss Poppy Pic
    WORKERS = int(os.environ.get("WORKERS", 8))
    ALLOW_EXCL = os.environ.get('ALLOW_EXCL', False)
    ALLOW_CHATS = os.environ.get("ALLOW_CHATS", True)

    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "sultan11100")
    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", "AM_YTSUPPORT")
    EVENT_LOGS = os.environ.get("EVENT_LOGS", "-1001841879487")
    JOIN_LOGGER = os.environ.get("JOIN_LOGGER", "-1001841879487")
    DEEP_API = os.environ.get("DEEP_API","c8e3d7fc-1f7e-455b-8019-5c1b7f21047a")
    OPENAI_KEY = os.environ.get("OPENAI_KEY","")
    WEBHOOK = bool(os.environ.get("WEBHOOK", False))
    CERT_PATH = os.environ.get("CERT_PATH")
    URL = os.environ.get("URL", "")  # Does not contain token
    PORT = int(os.environ.get("PORT", 5000))
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Morgana_tg_bot")
    BOT_NAME = os.environ.get("BOT_NAME", "Morgana")
    LOAD = os.environ.get("LOAD", "").split()
    NO_LOAD = os.environ.get("NO_LOAD","").split()

    DEL_CMDS = bool(os.environ.get("DEL_CMDS", True))
    INFOPIC = bool(os.environ.get("INFOPIC", False))
    REDIS_URL = os.environ.get("REDIS_URL","redis://default:mvwQl6zkrKuhD584XKB8kCOEB2Os8vlJ@redis-14834.c244.us-east-1-2.ec2.cloud.redislabs.com:14834")

else:
    from Yone.config import Development as Config

    TOKEN = Config.TOKEN

    try:
        OWNER_ID = int(Config.OWNER_ID)
    except ValueError:
        raise Exception("ʏᴏᴜʀ OWNER_ID ᴠᴀʀɪᴀʙʟᴇ ɪs ɴᴏᴛ ᴀ ᴠᴀʟɪᴅ ɪɴᴛᴇɢᴇʀ.")

    JOIN_LOGGER = Config.JOIN_LOGGER
    OWNER_USERNAME = Config.OWNER_USERNAME
    ALLOW_CHATS = Config.ALLOW_CHATS
    try:
        INSPECTOR = {int(x) for x in Config.INSPECTOR or []}
        DEV_USERS = {int(x) for x in Config.DEV_USERS or []}
    except ValueError:
        raise Exception(
            "ʏᴏᴜʀ sᴜᴅᴏ ᴏʀ ᴅᴇᴠ ᴜsᴇʀs ʟɪsᴛ ᴅᴏᴇs ɴᴏᴛ ᴄᴏɴᴛᴀɪɴ ᴠᴀʟɪᴅ ɪɴᴛᴇɢᴇʀs.")

    try:
        REQUESTER = {int(x) for x in Config.REQUESTER or []}
    except ValueError:
        raise Exception(
            "ʏᴏᴜʀ sᴜᴘᴘᴏʀᴛ ᴜsᴇʀs ʟɪsᴛ ᴅᴏᴇs ɴᴏᴛ ᴄᴏɴᴛᴀɪɴ ᴠᴀʟɪᴅ ɪɴᴛᴇɢᴇʀs.")

    INFOPIC = Config.INFOPIC
    EVENT_LOGS = Config.EVENT_LOGS
    WEBHOOK = Config.WEBHOOK
    PORT = Config.PORT
    CERT_PATH = Config.CERT_PATH
    API_ID = Config.API_ID
    API_HASH = Config.API_HASH
    DB_URI = Config.DATABASE_URL
    DEEP_API = Config.DEEP_API
    OPENAI_KEY = Config.OPENAI_KEY
    STRICT_GBAN = Config.STRICT_GBAN
    BOT_USERNAME = Config.BOT_USERNAME
    BOT_NAME = Config.BOT_NAME
    WORKERS = Config.WORKERS
    DEL_CMDS = Config.DEL_CMDS
    LOAD = Config.LOAD
    NO_LOAD = Config.NO_LOAD
    # CASH_API_KEY = Config.CASH_API_KEY
    REDIS_URL = Config.REDIS_URL
    SUPPORT_CHAT = Config.SUPPORT_CHAT
    # YOUTUBE_API_KEY = Config.YOUTUBE_API_KEY
    PHOTO = Config.PHOTO
    ALLOW_EXCL = Config.ALLOW_EXCL

INSPECTOR.add(OWNER_ID)
DEV_USERS.add(OWNER_ID)

updater = tg.Updater(TOKEN, workers=WORKERS, use_context=True)
pbot = Client("yonePyro", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)
telethn = TelegramClient("yoneuncle", API_ID, API_HASH)
dispatcher = updater.dispatcher

REDIS = StrictRedis.from_url(REDIS_URL, decode_responses=True)
try:
    REDIS.ping()
    LOGGER.info("Your redis server is now alive!")
except BaseException:
    raise Exception("Your redis server is not alive, please check again.")
finally:
    REDIS.ping()
    LOGGER.info("Your redis server is now alive!")
