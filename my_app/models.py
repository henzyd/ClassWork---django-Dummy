from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Hospital(models.Model):
    title = models.CharField(max_length=100)
    location = models.TextField()
    email = models.EmailField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.title} by {self.owner}'

    def get_absolute_url(self): ##### NOTE this is like redirect
        return reverse('detail_page', kwargs={'pk': self.id})