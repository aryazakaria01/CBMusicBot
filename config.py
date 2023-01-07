import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN"), 5890875137:AAHOz6jxV5MrHl5jXf2v57agNDo_XLnjXnc
BOT_NAME = getenv("BOT_NAME", "rolex")
BG_IMAGE = getenv("BG_IMAGE", 
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/e9a4d6655e5ddf51f9160.jpg")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/91034f175d41040d45b38.jpg")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/c8a0e9c544c5ea689caf9.jpg")
API_ID = int(getenv("26885114"))
API_HASH = getenv("41bb6d1f706da3bfbe95a820f427ae78")
BOT_USERNAME = getenv("BOT_USERNAME", "rolex")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "rolexjen")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "vanakam tamilnadu")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "rolexcorporation")
OWNER_NAME = getenv("OWNER_NAME", "surya") # isi dengan username kamu tanpa simbol @
PMPERMIT = getenv("PMPERMIT", None)
OWNER_ID = int(os.environ.get("5794915014")) # fill with your id as the owner of the bot
DATABASE_URL = os.environ.get("DATABASE_URL") # fill with your mongodb url
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL")) # make a private channel and get the channel id
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False)) # just fill with True or False (optional)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
LANG = getenv("LANG", "id")
