import asyncio
import logging

import telebot
from django.conf import settings
from django.core.management.base import BaseCommand

from bot.my_bot import bot

logging = logging.getLogger(__name__)

telebot.logger.setLevel(settings.LOG_LEVEL)

class Command(BaseCommand):
    help = "Запуск Бота"

    # def add_arguments(self, parser):
    #     parser.add_argument("poll_ids", nargs="+", type=int)

    def handle(self,  *args, **options):
        try:
            asyncio.run(bot.infinity_polling(logger_level=settings.LOG_LEVEL))
        except Exception as err:
            logging.error(f'Ошибка: {err}')

        # for poll_id in options["poll_ids"]:
        #     try:
        #         poll = Poll.objects.get(pk=poll_id)
        #     except Poll.DoesNotExist:
        #         raise CommandError('Poll "%s" does not exist' % poll_id)
        #
        #     poll.opened = False
        #     poll.save()
        #
        #     self.stdout.write(
        #         self.style.SUCCESS('Successfully closed poll "%s"' % poll_id)
        #     )
