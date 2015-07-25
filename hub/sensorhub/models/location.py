from django.db import models
from . import TimestampedModel


class Location(TimestampedModel):
    """
    Physical location (e.g. a specific building).
    """

    name = models.CharField(max_length=64)
    enabled = models.BooleanField(default=True, db_index=True)

    def __str__(self):
        return self.name
