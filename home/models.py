from django.db import models

class house(models.Model):
    name = models.CharField(max_length=100);
    price = models.CharField(max_length=20);
    region = models.CharField(max_length=100);
    img = models.ImageField(blank=True, upload_to='images/')


