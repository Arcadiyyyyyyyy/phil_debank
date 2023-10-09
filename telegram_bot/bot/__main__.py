import logging
import os

from dotenv import load_dotenv
from src.setup.config import Settings, configure_logging
from src.setup.bot_setup import bot_setup, generate_command_list

from telegram.ext import Application


def main():
    load_dotenv()
    configure_logging()
    Settings()

    bot = Application.builder().token(os.environ.get("TG_BOT_TOKEN")).post_init(generate_command_list).build()
    bot_setup(bot)

    logging.info("Started")
    bot.run_polling()


if __name__ == "__main__":
    main()
