from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from social.pipeline.partial import *

from .models import Profile


@partial
def save_profile(backend, user, response, *args, **kwargs):
    try:
        profile = Profile.objects.get(user=user)
        return
    except ObjectDoesNotExist:
        print("Error Occured. Could note create Profile")
        return redirect('complete_profile')
