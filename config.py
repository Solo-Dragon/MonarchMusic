from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/592cd4c7a71bfff068c70.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/0de13e91ac830f515a6e8.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/KazutoSupport")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/TheSungJinWoo")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5378543429").split()))


FAILED = "https://telegra.ph/file/3142c8040badb055748c2.jpg"
