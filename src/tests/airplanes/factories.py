import random

import factory

from airplanes.models import Airplane


class DefaultAirplaneFactory(factory.django.DjangoModelFactory):
    """
    Default AirplaneFactory
    """

    class Meta:
        model = Airplane

    passengers = random.randint(100, 1000)
