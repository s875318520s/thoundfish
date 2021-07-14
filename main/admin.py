from django.contrib import admin

# Register your models here.
from main.models import unit


class unitAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'status_1',
        'status_2',
        'status_1_change',
        'status_2_change',
        'status_1_uesr',
        'status_2_uesr',
    )


admin.site.register(unit, unitAdmin)