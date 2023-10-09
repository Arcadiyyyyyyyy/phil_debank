from enum import Enum

from telegram.ext import Application, CommandHandler

from bot.src.front_end.commands.top_reward import command_top_reward


class Commands(Enum):
    # c = command, d = description
    hot_list_top_reward = {"c": "hlrt", "d": "Получить топ постов по донатам из горячих постов"}


async def generate_command_list(application: Application):
    command_list = []
    for x in [command.value for command in Commands]:
        command_list.append(
            (x.get("c"), x.get("d"))
        )
    await application.bot.set_my_commands(command_list)


def bot_setup(bot: Application):
    bot.add_handler(CommandHandler(Commands.hot_list_top_reward.value.get("c"), command_top_reward))
