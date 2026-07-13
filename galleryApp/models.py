from django.db import models
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, max_length=500)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
 
    def __str__(self):
        return self.user.username
    
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
 
    def __str__(self):
        return self.name


