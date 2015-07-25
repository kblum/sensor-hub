from django.db import models
from django.utils import timezone


class TimestampedModel(models.Model):
    """
    Abstract model that provides automatic timestamp fields for creation and modification.
    Exists as a base class for all application models.
    """

    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        """
        Update timestamps when saving.
        """
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(TimestampedModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True
