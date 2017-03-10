import hashlib

from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse, NoReverseMatch
from django.core.validators import RegexValidator, URLValidator
from django.db import models
from ckeditor_uploader import fields
from django.db.models.signals import post_save
from django.dispatch import receiver


lowercaseAlphabet = RegexValidator(
    r'^[a-z]*$', 'Only lower case alphabets are allowed.')


def validate_navbar_entry(url):
    domain = Site.objects.get_current().domain
    try:
        reverse(url)
    except NoReverseMatch:
        try:
            URLValidator()(url)
        except ValidationError:
            URLValidator()('https://%s%s' % (domain, url))
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


class Keynote(models.Model):
    "Stores information about the keynote speech or talk in the fest"

    # keynote id
    identifier = models.CharField(max_length=50, unique=True,
                                  validators=[lowercaseAlphabet])

    # keynote name
    name = models.CharField(max_length=255)

    # keynote description
    description = models.TextField()

    # keynote image
    image = models.ImageField(upload_to='event_images/',
                              blank=True, null=True)

    # keynote venue
    venue = models.CharField(max_length=255)

    # keynote date and time
    date_time = models.DateTimeField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/keynote/%s/' % self.identifier


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


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    # create a dummy profile for superuser
    if created and instance.is_superuser:
        Profile.objects.create(user=instance)
        instance.profile.save()


class organizerMember(models.Model):
    """Stores information about the members of the organization
    that is conducting the fest"""

    name = models.CharField(max_length=100)

    position = models.CharField(max_length=100)

    rank = models.IntegerField(default=0)

    avatar_img = models.ImageField(upload_to='avatar_images/',
                                   blank=True, null=True)

    contactNumber = models.CharField(max_length=15)

    emailId = models.EmailField(blank=True, null=True)

    contactURL = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Sponsor(models.Model):
    """Stores information about fest sponsors
    """
    name = models.CharField(max_length=100)

    logo = models.ImageField(upload_to='sponsor_logos/')

    rank = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class About(models.Model):
    """Stores about content as raw html
    """
    identifier = models.CharField(max_length=50, unique=True)
    content = fields.RichTextUploadingField()

    def __str__(self):
        return self.identifier

    class Meta:
        verbose_name = "about"
        verbose_name_plural = "about"


class NewsLetter(models.Model):
    """Stores newsletters sent to subscribed users
    """
    identifier = models.CharField(max_length=50, unique=True)
    content = fields.RichTextUploadingField()

    def __str__(self):
        return self.identifier


class Subscription(models.Model):
    """Stores the details of subscribed users
    """
    identifier = models.CharField(max_length=50, unique=True)
    contact_email = models.EmailField(unique=True)

    def save(self, *args, **kwargs):
        """On save, add unique identifier
        """
        hasher = hashlib.md5(self.contact_email.encode())
        self.identifier = hasher.hexdigest()
        return super(Subscription, self).save(*args, **kwargs)

    def __str__(self):
        return self.contact_email


class FAQ(models.Model):
    """Stores the frequently asked questions
    """
    identifier = models.CharField(max_length=50, unique=True)
    question = fields.RichTextUploadingField()
    answer = fields.RichTextUploadingField()

    def __str__(self):
        return self.identifier

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'


class NavbarEntry(models.Model):
    """Stores the navigation bar entries
    """
    url = models.CharField(default='#', max_length=100,
        validators=[validate_navbar_entry])
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Navbar Entry'
        verbose_name_plural = 'Navbar Entries'
