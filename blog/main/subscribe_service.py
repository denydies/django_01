from django.core.exceptions import ObjectDoesNotExist

from .models import Subscriber


def subscribe(author_id, email_to):
    try:
        Subscriber.objects.get(email_to=email_to, author=author_id)
    except ObjectDoesNotExist:
        subscriber = Subscriber(email_to=email_to, author=author_id)
        subscriber.save()

#
# def subscriber(author_id, email_to, author=None):
#     try:
#         Subscriber.object.get(email_to=email_to, author=author)
#     except ObjectDoesNotExist:
#         subscriber = Subscriber(email_to=email_to, author_id=author_id)
#         subscriber.save()
# from django.shortcuts import redirect, render
#
# from blog.main.forms import SubscriberForm


# #def subs_add(request):
#     error = ""
#     if request.method == "SUBSCRIBE":
#         form = SubscriberForm(request.SUBSCRIBE)
#         if form.is_valid():
#             form.save()
#             return redirect('subs')
#         else:
#             error = 'Error on save Subscribe'
#     else:
#         form = SubscriberForm()
#     context = {
#         'form': form,
#         'err': error
#     }
#     return render(request, 'main/subscribe_add.html', context=context)
