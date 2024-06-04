import asyncio
import logging

import telebot
from django.conf import settings
from django.core.management.base import BaseCommand
from django.config import settings

from bot.my_bot import bot

<<<<<<< HEAD
logger = logging.getLogger(__name__)

=======
logging = logging.getLogger(__name__)

telebot.logger.setLevel(settings.LOG_LEVEL)
>>>>>>> 8c5bbe63ccf81da9af0f8db865bc301f5ded00d8

class Command(BaseCommand):
    help = "Запуск Бота"

    # def add_arguments(self, parser):
    #     parser.add_argument("poll_ids", nargs="+", type=int)

<<<<<<< HEAD
    def handle(self, *args, **options):
=======
    def handle(self,  *args, **options):
>>>>>>> 8c5bbe63ccf81da9af0f8db865bc301f5ded00d8
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
