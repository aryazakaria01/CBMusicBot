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
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/6790864f5fe27471bdc8d.png")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/9dd2e33db6b44b8417e75.png")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/a0ea0493999274797f23c.jpg")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/a0ea0493999274797f23c.jpg")
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
