from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()

    def __str__(self):
        return self.name


class Merch(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    date = models.DateTimeField("date published", default=timezone.now)
    stock = models.IntegerField(default=0)
    category = models.ForeignKey(to=Category, on_delete=models.PROTECT)
