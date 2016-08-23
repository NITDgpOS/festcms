from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    "Stores additional information about the user"
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user
