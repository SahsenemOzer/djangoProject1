from django.db import models


class house(models.Model):
    name = models.CharField(max_length=100);
    price = models.CharField(max_length=20);
    region = models.CharField(max_length=100);
    img = models.ImageField(blank=True, upload_to='images/')


class comment(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    yorum = models.CharField(max_length=400)
    houseid = models.CharField(max_length=15)


class mesaj(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    baslik = models.CharField(max_length=40)
    mesaj = models.CharField(max_length=400)

