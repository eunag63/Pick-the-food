from django.contrib import admin

# Register your models here.
from .models import Food, Post


admin.site.register(Food)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'formatted_hit_count',)

    def formatted_hit_count(self, obj):
        return obj.current_hit_count if obj.current_hit_count > 0 else '-'
    formatted_hit_count.admin_order_field = 'hit_count'
    formatted_hit_count.short_description = 'Hits'

admin.site.register(Post, PostAdmin)
