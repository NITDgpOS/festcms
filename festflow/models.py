from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Event(models.Model):
    "Stores information about the events in the fest"

    # event name
    name = models.CharField(max_length=255)

    # event description
    description = models.TextField()

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
