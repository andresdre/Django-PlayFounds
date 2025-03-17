from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class Activity(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class PlayFound(models.Model):
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='playfounds/', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="playfounds")
    activities = models.ManyToManyField(Activity, related_name='playfounds')

    def get_absolute_url(self):
        return reverse('playfounds-detail', kwargs={'pk': self.id})
    
    def __str__(self):
        return self.name

