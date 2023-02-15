from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.
class Agent(models.Model):
    name = models.CharField(max_length = 150)
    biodata=models.TextField()
    email=models.EmailField()
    phone=models.CharField(max_length=150)
    image=models.ImageField(upload_to='realtor')
    top_seller=models.BooleanField(default=False)
    date_hired=models.DateField(default=timezone.now())
    def __str__(self):
        return self.name