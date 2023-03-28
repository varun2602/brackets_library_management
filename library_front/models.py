from django.db import models 
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    name = models.CharField(max_length = 50, blank = True, null = True)
    groups = models.ManyToManyField(
        'auth.Group', related_name='custom_user_groups', blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission', related_name='custom_user_permissions', blank=True
    )
  
    def __str__(self):
        return f"{self.username}"
