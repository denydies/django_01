from celery import shared_task
from time import sleep

from .services import notify_service
from .services.notify_service import email_send

@shared_task
def noyify_async(email_to, author_name):
    print("------tasks: noyify_async - START")
    email_send(email_to, author_name)
    print("------tasks: noyify_async - FINISH")

#
# @shared_task
# def subscribe_notify_beat():
#     a = email_all()
#     print("------tasks: noyify_async - START")
#     print(a)
#     print("------tasks: noyify_async - FINISH")

# cron beat time (0 9 * * *) - каждый день в 9 утра
# @shared_task
# def subscribe_notify_beat(email_to):
# https://tproger.ru/wp-content/plugins/citation-widget/get-quote.php
