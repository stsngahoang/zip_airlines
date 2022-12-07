import random

import factory

from airplanes.models import AirPlane


class DefaultAirPlaneFactory(factory.django.DjangoModelFactory):
    """
    Default AirPlaneFactory
    """

    class Meta:
        model = AirPlane

    passengers = random.randint(100, 1000)
