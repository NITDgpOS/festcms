from django.shortcuts import render, redirect

from .forms import EditProfileForm
from .models import User, Profile

# Create your views here.


def index(request):
    context = {}
    profiles_count = Profile.objects.count()

    context['profiles_count'] = profiles_count
    return render(request, 'festflow/index.html', context)


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
