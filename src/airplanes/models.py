import math

from django.db import models

from .constants import (
    AIRPLANE_CONSUMPTION_LITERS,
    AIRPLANE_DEFAULT_CAPACITY,
    PASSENGER_ADDITIONAL_FUEL_CONSUMPTION,
)


# Create your models here.
class Airplane(models.Model):
    passengers = models.PositiveIntegerField()

    class Meta:
        db_table = "airplane"
        ordering = ("-id",)

    @property
    def fuel_tanks_capacity(self):
        return AIRPLANE_DEFAULT_CAPACITY * self.id

    @property
    def fuel_consumption_per_minutes(self):
        return (
            math.log(self.id * AIRPLANE_CONSUMPTION_LITERS)
            + self.passengers * PASSENGER_ADDITIONAL_FUEL_CONSUMPTION
        )

    @property
    def maximum_minutes_able_to_fly(self):
        if self.fuel_consumption_per_minutes:
            return self.fuel_tanks_capacity / self.fuel_consumption_per_minutes
        else:
            # @TODO: Raise exception
            return None
