# accounts/models.py

from django.db import models
from django.contrib.auth.models import User



class UserProfile(models.Model):
    # This links the UserProfile to a specific Django User
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # Add a field to distinguish between drivers and coaches
    is_coach = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

