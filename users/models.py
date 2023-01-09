from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(verbose_name='Photo', upload_to='user_image', null=True, blank=True)

    def __str__(self):
        return self.first_name
