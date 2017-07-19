from django.db import models
from . import TimestampedModel, EnabledQuerySet, Deployment


SERIAL_NUMBER_PREFIX = '0x'


class Sensor(TimestampedModel):
    """
    Temperature sensor.
    """

    name = models.CharField(max_length=64)
    serial_number = models.CharField(max_length=16)
    enabled = models.BooleanField(default=True, db_index=True)
    deployment = models.ForeignKey(Deployment, on_delete=models.CASCADE, null=False, blank=False)

    objects = EnabledQuerySet.as_manager()

    def save(self, *args, **kwargs):
        self.serial_number = self._process_serial_number(self.serial_number)
        super(Sensor, self).save(*args, **kwargs)

    @staticmethod
    def _process_serial_number(raw_serial_number):
        # ensure that serial number is lowercase and remove '0x' prefix
        serial_number = raw_serial_number.lower()
        if serial_number.startswith(SERIAL_NUMBER_PREFIX):
            serial_number = serial_number[len(SERIAL_NUMBER_PREFIX):]
        return serial_number

    @staticmethod
    def get_sensor(serial_number):
        return Sensor.objects.enabled().get(serial_number__iexact=Sensor._process_serial_number(serial_number))

    def __str__(self):
        return self.serial_number
