from django.core.exceptions import ObjectDoesNotExist
from social_core.pipeline.partial import *

from .models import Profile


@partial
def save_profile(strategy, details, user=None, is_new=False, *args, **kwargs):
    try:
        profile = Profile.objects.get(user=user)
        return
    except ObjectDoesNotExist:
        print("Error Occured. Could note create Profile")
        return strategy.redirect('complete_profile')
