from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import CallbackContext

from telegram_bot.bot.src.back_end.Debank import Debank
from telegram_bot.bot.src.exceptions.back_end.DebankAPI import DebankAPIError


async def command_top_reward(update: Update, context: CallbackContext):
    try:
        if context.args:
            text = Debank.get_top_reward(int(context.args[0]))
        else:
            text = Debank.get_top_reward()
    except DebankAPIError:
        text = f"Произошла ошибка. Попробуйте ещё раз, или напишите программистам если ситуация повториться."
    except ValueError:
        text = f'Неправильный аргумент у команды'

    await context.bot.send_message(
        update.effective_chat.id,
        text,
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True
    )
