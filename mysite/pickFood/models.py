from django.db import models

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=20)
    introduction = models.TextField()

    def __str__(self):
        return self.name

class Count(models.Model):
    num = models.IntegerField(default = 0)
