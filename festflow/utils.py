from email_extras.utils import send_mail_template
from django.shortcuts import Http404

from .models import *
# Create your utility functions here.


def send_subscription_success(from_addr, to_addr, template):
    context = {'email': to_addr}
    send_mail_template(
        "New Subscription",
        template,
        from_addr,
        to_addr,
        fail_silently=False,
        context=context,)


def unsubscribe(id):
    try:
        subscription = Subscription.objects.get(identifier=id)
        mail = subscription.contact_email
        subscription.delete()
        return mail
    except Subscription.DoesNotExist:
        raise Http404
