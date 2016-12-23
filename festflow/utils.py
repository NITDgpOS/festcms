from django.core.mail import send_mail
from django.shortcuts import Http404

from .models import *
# Create your utility functions here.


def send_subscription_success(from_addr, to_addr, template):
    content = template.render({
        'email': to_addr
    })

    send_mail(
        "New Subscription",
        content,
        from_addr,
        [to_addr],
        fail_silently=False,)


def unsubscribe(id):
    try:
        subscription = Subscription.objects.get(identifier=id)
        mail = subscription.contact_email
        subscription.delete()
        return mail
    except Subscription.DoesNotExist:
        raise Http404

