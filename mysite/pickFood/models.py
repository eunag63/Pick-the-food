from django.db import models

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=20)
    introduction = models.TextField()

    def __str__(self):
        return self.name



class Counts(models.Model):
    view_count = models.IntegerField(default=0)
    
    @property
    def update_counter(self):
        self.view_count = self.view_count + 1
        self.save()
