from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, related_name='user_profile', on_delete=models.CASCADE)

    first_name = models.CharField(max_length=264, blank=True)
    last_name = models.CharField(max_length=264, blank=True)
    email = models.EmailField(unique=True, null=False)
    dob = models.DateField(blank=True, null=True)
    address = models.TextField(max_length=300, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics')

    def __str__(self):
        return str(self.user)
