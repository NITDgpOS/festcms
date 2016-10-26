from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models


lowercaseAlphabet = RegexValidator(
    r'^[a-z]*$', 'Only lower case alphabets are allowed.')
# Create your models here.


class Event(models.Model):
    "Stores information about the events in the fest"

    # event id
    identifier = models.CharField(max_length=50, unique=True,
                                  validators=[lowercaseAlphabet])

    # event name
    name = models.CharField(max_length=255)

    # event description
    description = models.TextField()

    # event logo
    logo = models.ImageField(upload_to='event_images/',
                             blank=True, null=True)

    # event problem statement file
    problem_statement_file = models.FileField(upload_to='problem_statements/',
                                              blank=True, null=True)

    # event venue
    venue = models.CharField(max_length=255)
    venue_lat = models.DecimalField(max_digits=9, decimal_places=8,
                                    blank=True, null=True)
    venue_lon = models.DecimalField(max_digits=9, decimal_places=8,
                                    blank=True, null=True)

    # event date and time
    date_time = models.DateTimeField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/events/%s/' % self.identifier


class Profile(models.Model):
    "Stores additional information about the user"

    # each profile is associated with a user
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # profile informations:
    institute_name = models.CharField(max_length=255)
    degree_name = models.CharField(max_length=255)
    major_subject_name = models.CharField(max_length=255)

    phone_number = models.CharField(max_length=15)

    # events registered for
    registered_events = models.ManyToManyField(Event)

    def __str__(self):
        return self.user.get_full_name()

    def get_absolute_url(self):
        return '/events/%s/' % self.user.username


class organizerMember(models.Model):
    """Stores information about the members of the organization
    that is conducting the fest"""

    name = models.CharField(max_length=100)

    position = models.CharField(max_length=100)

    rank = models.IntegerField(default=0)

    avatar_img = models.ImageField(upload_to='avatar_images/',
                                   blank=True, null=True)

    contactNumber = models.CharField(max_length=15)

    contactURL = models.URLField()

    def __str__(self):
        return self.name


class sponsor(models.Model):
    """Stores information about fest sponsors
    """
    name = models.CharField(max_length=100)

    logo = models.ImageField(upload_to='sponsor_logos/')

    rank = models.IntegerField(default=0)
