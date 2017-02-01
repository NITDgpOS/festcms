from django.forms import ModelForm
from .models import *


class EditProfileForm(ModelForm):

    class Meta:
        model = Profile
        fields = ['institute_name', 'degree_name',
                  'major_subject_name', 'phone_number']


class SubscriptionForm(ModelForm):

    class Meta:
        model = Subscription
        fields = ['contact_email']
