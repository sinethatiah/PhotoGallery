from django.db import models
from django.conf import settings
from cloudinary.models import CloudinaryField

# Create your models here.

    
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
 
    def __str__(self):
        return self.name


class Photo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = CloudinaryField('image')
    tags = models.ManyToManyField(Tag, related_name='photos', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
class PhotoInteraction(models.Model):
    LIKE = 'like'
    DISLIKE = 'dislike'
    CHOICES = [(LIKE, 'Like'), (DISLIKE, 'Dislike')]
 
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name='interactions')
    interaction_type = models.CharField(max_length=7, choices=CHOICES)
 
    class Meta:
        unique_together = ('user', 'photo')
 
    def __str__(self):
        return f"{self.user.username} - {self.interaction_type} - {self.photo.title}"  
     
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, max_length=500)
    profile_picture = CloudinaryField('image', blank=True, null=True)