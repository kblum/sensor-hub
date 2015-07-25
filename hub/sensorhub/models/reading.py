from django.db import models
from . import TimestampedModel, Sensor, Deployment


class Reading(TimestampedModel):
    """
    Reading from a specific temperature sensor.
    """

    sensor = models.ForeignKey(Sensor, null=False, blank=False)
    deployment = models.ForeignKey(Deployment, null=False, blank=False)
    temperature = models.FloatField(null=False, blank=False)

    def __str__(self):
        return "Temperature: %.2f" % self.temperature
