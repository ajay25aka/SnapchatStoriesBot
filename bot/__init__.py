import logging
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


class ENV_VARS(object):
    API_ID = int(os.environ.get("API_ID", "26173059"))
    API_HASH = os.environ.get("API_HASH", "4b5337555b3b5ee8b8e4d02c36fd665d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6085449506:AAGO152_HKpsTNGk107Yt1TjAXxW8EZLfNM")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Content_saver2_bot")
    #AUTH_USER = int(os.environ.get("AUTH_USER", 5071059420))


Config = ENV_VARS

handler = Config.BOT_USERNAME


class CMD(object):
    START = ["start", f"start@{handler}"]
