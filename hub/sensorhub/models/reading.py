from django.db import models
from . import TimestampedModel, Sensor, Deployment


class Reading(TimestampedModel):
    """
    Reading from a specific temperature sensor.
    """

    sensor = models.ForeignKey(Sensor, null=False, blank=False)
    deployment = models.ForeignKey(Deployment, null=False, blank=False)
    temperature = models.FloatField(null=False, blank=False)

    @staticmethod
    def create_temperature_reading(sensor, temperature, save=False):
        """
        Create a new temperature reading.

        :param sensor: the sensor from which the reading was made
        :type sensor: Sensor
        :param temperature: the value of the temperature reading from the sensor
        :type temperature: float
        :param save: set to True if the reading should be saved after being created, False if not
        :return: temperature reading
        :rtype : Reading
        """
        deployment = sensor.deployment  # record current deployment of sensor (sensor deployment may change in future)
        reading = Reading(sensor=sensor, deployment=deployment, temperature=temperature)
        if save:
            reading.save()
        return reading

    def __str__(self):
        return "Temperature: %.2f" % self.temperature
