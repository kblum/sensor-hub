from django.db import models
from . import TimestampedModel, Location


class Deployment(TimestampedModel):
    """
    Specific area within a location (e.g. a room within a building), where a sensor is positioned.
    """

    name = models.CharField(max_length=64)
    enabled = models.BooleanField(default=True, db_index=True)
    location = models.ForeignKey(Location, null=False, blank=False)
    description = models.TextField(null=False, blank=True)

    def __str__(self):
        return self.name
