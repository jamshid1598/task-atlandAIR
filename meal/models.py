from django.db import models

# Create your models here.


class Meal(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    category = models.CharField(max_length=200, blank=True, null=True)
    instruction = models.TextField(blank=True, null=True)
    region = models.CharField(max_length=200, blank=True, null=True)
    image = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.name