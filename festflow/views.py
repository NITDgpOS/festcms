from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, Http404

from .forms import EditProfileForm
from .models import *

# Create your views here.


def index(request):
    context = {}
    profiles_count = Profile.objects.count()
    all_events = Event.objects.all()

    context['profiles_count'] = profiles_count
    context['all_events'] = all_events
    return render(request, 'festflow/index.html', context)


def event_view(request, event_identifier):
    context = {}
    try:
        event = Event.objects.get(identifier=event_identifier)
    except ObjectDoesNotExist:
        raise Http404

    context['event'] = event

    return render(request, 'festflow/event_view.html', context)


def complete_profile(request):
    context = {}
    backend = request.session['partial_pipeline']['backend']
    user_id = request.session['partial_pipeline']['kwargs']['user']
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
