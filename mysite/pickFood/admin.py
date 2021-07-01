from django.contrib import admin

# Register your models here.
from .models import Food, Post


admin.site.register(Food)
admin.site.register(Post)
