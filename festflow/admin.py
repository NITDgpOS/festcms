from django.contrib import admin
from django.conf import settings
from django.core.mail import send_mass_mail
from django.template.loader import get_template
from django.contrib.sites.shortcuts import get_current_site

from .models import *
# Register your models here.


def send_email(modeladmin, request, queryset):
    our_email = settings.DEFAULT_FROM_EMAIL
    users = Subscription.objects.all()
    recipients = [user.contact_email for user in users]
    messages = []
    site = get_current_site(request)
    template = get_template('festflow/newsletter.html')
    for user in users:
        for newsletter in queryset:
            content = template.render({
                'newsletter': newsletter.content,
                'url': 'http://%s/subscribe?unsubscribe=%s' % (
                    site, user.identifier),
            })
            messages.append((
                "Newsletter",
                content,
                our_email,
                recipients))

    send_mass_mail(messages, fail_silently=False)


class NewsLetterAdmin(admin.ModelAdmin):
    actions = [send_email]


admin.site.register(Profile)
admin.site.register(Event)
admin.site.register(organizerMember)
admin.site.register(Sponsor)
admin.site.register(About)
admin.site.register(Subscription)
admin.site.register(NewsLetter, NewsLetterAdmin)
admin.site.register(FAQ)
admin.site.register(NavbarEntry)
admin.site.register(Keynote)
