from django.db import models
from . import TimestampedModel, Deployment


class Sensor(TimestampedModel):
    """
    Temperature sensor.
    """

    serial_number = models.CharField(max_length=16)
    enabled = models.BooleanField(default=True, db_index=True)
    deployment = models.ForeignKey(Deployment, null=False, blank=False)

    def __str__(self):
        return self.serial_number
