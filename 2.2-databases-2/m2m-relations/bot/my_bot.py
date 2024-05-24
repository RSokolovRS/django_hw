import aiohttp
import logging

from django.template.defaultfilters import pprint
from telebot.async_telebot import AsyncTeleBot

from django.conf import settings
from telebot.types import ChatMemberUpdated

bot = AsyncTeleBot(settings.TOKEN_BOT, parse_mode='HTML')
logging = logging.getLogger(__name__)


@bot.chat_member_handler(ChatMemberUpdated)
async def chat_member_handler_bot(message):
    logging.info(f'вот {message}')
    pprint(f'вот {message}')
    # text = 'Новый подписчик!'
    # await bot.send_message(message.chat.id, text)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    text = 'Привет Друг'
    await bot.send_message(message.chat.id, text)


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    await bot.reply_to(message, message.text)


# asyncio.run(bot.polling())
