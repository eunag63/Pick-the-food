from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=20)
    introduction = models.TextField()

    def __str__(self):
        return self.name
