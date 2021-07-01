from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from hitcount.models import HitCountMixin, HitCount
# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=20)
    introduction = models.TextField()

    def __str__(self):
        return self.name



class Post(models.Model, HitCountMixin):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    published_on = models.DateTimeField(blank=True, default=None, null=True)
    content = models.TextField(blank=True)

    hit_count_generic = GenericRelation(
        HitCount, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation'
    )

    def current_hit_count(self):
        return self.hit_count.hits
