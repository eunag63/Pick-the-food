from django.contrib import admin

# Register your models here.
from .models import Food, Counts


admin.site.register(Food)
admin.site.register(Counts)
