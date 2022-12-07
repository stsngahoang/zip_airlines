from django.contrib import admin

from .models import Airplane

# Register your models here.


class AirplaneAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "passengers",
        "fuel_tanks_capacity",
        "fuel_consumption_per_minutes",
        "maximum_minutes_able_to_fly",
    )


admin.site.register(Airplane, AirplaneAdmin)
