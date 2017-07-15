from django.db import models
from . import TimestampedModel, Sensor, Deployment, UserAgent


class Reading(TimestampedModel):
    """
    Reading from a specific temperature sensor.
    """

    sensor = models.ForeignKey(Sensor, null=False, blank=False)
    deployment = models.ForeignKey(Deployment, null=False, blank=False)
    temperature = models.FloatField(null=False, blank=False)
    user_agent = models.ForeignKey(UserAgent, null=True, blank=True)

    @staticmethod
    def create_temperature_reading(sensor, temperature, user_agent, save=False):
        """
        Create a new temperature reading.

        :param sensor: the sensor from which the reading was made
        :type sensor: Sensor
        :param temperature: the value of the temperature reading from the sensor
        :type temperature: float
        :param user_agent: current user agent of device creating the reading (optional)
        :type user_agent: UserAgent
        :param save: set to True if the reading should be saved after being created, False if not
        :return: temperature reading
        :rtype : Reading
        """
        deployment = sensor.deployment  # record current deployment of sensor (sensor deployment may change in future)
        reading = Reading(sensor=sensor, deployment=deployment, temperature=temperature, user_agent=user_agent)
        if save:
            reading.save()
        return reading

    def __str__(self):
        return "Temperature: %.2f" % self.temperature
