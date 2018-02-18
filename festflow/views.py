from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.shortcuts import render, redirect, Http404
from social_core.pipeline.utils import partial_load
from social_django.utils import load_strategy

from .forms import *
from .models import *
from .utils import *

# Create your views here.


def index(request):
    context = {}
    profiles_count = Profile.objects.count()
    all_events = Event.objects.all()

    context['profiles_count'] = profiles_count
    context['all_events'] = all_events

    return render(request, 'festflow/index.html', context)


def about(request):
    context = {}
    context['content'] = About.objects.last()
    return render(request, 'festflow/about.html', context)


def events(request):
    context = {}
    all_events = Event.objects.all()
    context['all_events'] = all_events
    return render(request, 'festflow/event.html', context)


def keynotes(request):
    context = {}
    all_events = Keynote.objects.all()
    context['all_keynotes'] = all_events
    return render(request, 'festflow/keynote.html', context)


def sponsors(request):
    context = {}
    all_sponsors = Sponsor.objects.all()
    context['all_sponsors'] = all_sponsors
    return render(request, 'festflow/sponsors.html', context)


def contact(request):
    context = {}
    all_contacts = organizerMember.objects.all()
    context['all_contacts'] = all_contacts
    return render(request, 'festflow/contact.html', context)


def reachus(request):
    context = {}
    context["google_api_key"] = settings.GOOGLE_API_KEY
    return render(request, 'festflow/reachus.html', context)


def faq(request):
    context = {}
    context['faqs'] = FAQ.objects.all()
    return render(request, 'festflow/faq.html', context)


def login_page(request):
    context = {}
    profiles_count = Profile.objects.count()
    context['profiles_count'] = profiles_count
    return render(request, 'festflow/login_page.html', context)


def event_view(request, event_identifier):
    context = {}
    try:
        event = Event.objects.get(identifier=event_identifier)
    except ObjectDoesNotExist:
        raise Http404

    if request.user.is_authenticated():
        user_profile = Profile.objects.get(user=request.user)
        context['user_profile'] = user_profile

    context['event'] = event

    return render(request, 'festflow/event_view.html', context)


def keynote_view(request, keynote_identifier):
    context = {}
    try:
        keynote = Keynote.objects.get(identifier=keynote_identifier)
    except ObjectDoesNotExist:
        raise Http404

    if request.user.is_authenticated():
        user_profile = Profile.objects.get(user=request.user)
        context['user_profile'] = user_profile

    context['keynote'] = keynote

    return render(request, 'festflow/keynote_view.html', context)


@login_required
def register_event(request, event_identifier):
    try:
        event = Event.objects.get(identifier=event_identifier)
    except ObjectDoesNotExist:
        raise Http404

    user_profile = Profile.objects.get(user=request.user)
    user_profile.registered_events.add(event)
    user_profile.save()

    return redirect(event.get_absolute_url())


def complete_profile(request):
    strategy = load_strategy(request)
    partial = partial_load(strategy, request.session['partial_pipeline_token'])
    context = {}
    backend = partial.backend;
    user_id = partial.kwargs['user'].id;
    user_obj = User.objects.get(id=user_id)

    if request.method == 'POST':
        profile_form = EditProfileForm(request.POST)
        if profile_form.is_valid():
            new_profile = profile_form.save(commit=False)
            new_profile.user = user_obj
            new_profile.save()
            return redirect('/complete/%s' % backend)
    else:
        profile_form = EditProfileForm()

    context['user'] = user_obj
    context['backend'] = backend
    context['profile_form'] = profile_form
    return render(request, 'festflow/complete_profile.html', context)


def subscribe(request):
    context = {}

    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        to_addr = request.POST.get('contact_email', '')
        if Subscription.objects.filter(contact_email=to_addr).count():
            context['result'] = ('Your email: %s has already'
                                 ' been subscribed.' % to_addr)
        elif form.is_valid():
            form.save()
            send_subscription_success(
                from_addr=settings.DEFAULT_FROM_EMAIL,
                to_addr=to_addr,
                template='subscribed_email',)
            context['result'] = ('Your email: %s is successfully'
                                 ' subscribed.' % to_addr)
    else:
        form = SubscriptionForm
        context['subscription_form'] = form
        id = request.GET.get('unsubscribe', '')
        if len(id) != 0:
            context['unsubscribe'] = unsubscribe(id)

    return render(request, 'festflow/subscribe.html', context)
