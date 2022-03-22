import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    label = models.CharField(max_length=50)
    slug = models.SlugField()
    parent = models.IntegerField()
    def __str__(self):
        return "%s" % (self.label)

class Product(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    reference = models.CharField(max_length=60)
    description = models.CharField(max_length=255)
    price = models.FloatField()
    categories =  models.ManyToManyField(Category)
    exchange = models.BooleanField(blank=False)
    donation = models.BooleanField(blank=False)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

