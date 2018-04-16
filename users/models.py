import random

from django.urls import reverse
from django.db import models


# extending User model
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    random_number = models.IntegerField(default=round(random.random() * 100))
    birthday = models.DateField(null=True)

    def get_absolute_url(self):
        return reverse('users:user-list')


