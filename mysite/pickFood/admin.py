from django.contrib import admin

# Register your models here.
from .models import Food, Count


admin.site.register(Food)
admin.site.register(Count)
