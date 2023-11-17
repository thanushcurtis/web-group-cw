from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(max_length=254, unique=True)
    profile_image = models.ImageField(upload_to="api\static\api\spa\assets\profile_images", null=True, blank=True)
    dob = models.DateField(default=date.today)
