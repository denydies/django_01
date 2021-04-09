from django.core.exceptions import ObjectDoesNotExist

from .models import Subscriber

#
# def subscriber(author_id, email_to):
#     try:
#         Subscriber.object.get(email_to=email_to, author=author)
#     except ObjectDoesNotExist:
#         subscriber = Subscriber(email_to=email_to, author_id=author_id)
#         subscriber.save()
