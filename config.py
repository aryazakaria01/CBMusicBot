import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "ᴄʏʙᴇʀ ᴍᴜsɪᴄ ʙᴏᴛ")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/ec11307dd8a3496d8dcbf.jpg")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/bad69dc7929731b11e056.jpg")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/49342251174d89e1a671e.png")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/5c4e60fc17c45d56f39e8.png")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME", "CyberMusikBot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "SaitamaHelper")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "CyberSupportGroup")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "CyberMusicProject")
OWNER_NAME = getenv("OWNER_NAME", "Badboyanim") # isi dengan username kamu tanpa simbol @
DEV_NAME = getenv("DEV_NAME", "Badboyanim")
PMPERMIT = getenv("PMPERMIT", None)

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
