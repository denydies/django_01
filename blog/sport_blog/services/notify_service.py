from django.core.mail import send_mail

# from django.http import request, JsonResponse


#
# def notify(email_to):
#     email_send(email_to)
#     telegram_notify(email_to)
#
#
# def telegram_notify(email_to):
#     Telegram()
#     Telegram.notify()
#
#
# class Telegram:
#     def notefy(self, msg):
#         telegram_url = 'https://api.telegram.org/bot<Token>'
#         params = {'chat_id': 'hello', 'text': msg}
#         response = request.post(telegram_url + 'sendMessage', data=params)
#
#         return response


def email_send(email_to, author_name):
    send_mail(
        'Sport Blog',
        'Вы подписались на автора : {}'.format(author_name),
        'denistest13@gmail.com',
        [email_to],
        fail_silently=False
    )
