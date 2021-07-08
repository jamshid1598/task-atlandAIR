from django.contrib import admin

from .models import Meal

# Register your models here.

class MealAdmin(admin.ModelAdmin):
    list_display=('name', 'category', 'region')

    fieldsets=(
        ('Meal', {
            'fields': (
                'name', 'slug', 'category', 'region', 'instruction', 'image',  
            )
        }),
    )

admin.site.register(Meal, MealAdmin)
