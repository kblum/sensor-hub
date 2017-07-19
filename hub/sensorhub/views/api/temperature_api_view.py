import logging
from . import BaseAuthenticatedApiView
from hub.sensorhub.models import Sensor, Reading, UserAgent
from rest_framework.exceptions import ParseError
from rest_framework.response import Response

logger = logging.getLogger(__name__)


class TemperatureApiView(BaseAuthenticatedApiView):
    """
    View for temperature API.
    Allows temperature readings to be recorded through POST requests.
    """

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        logger.info("Temperature API POST request: %s", request.data)

        request_readings = request.data.get('readings', None)
        if request_readings is None:
            raise ParseError("Invalid request; 'readings' must be included")

        if not isinstance(request_readings, dict):
            raise ParseError("Invalid request; 'readings' must be an object/dictionary")

        for serial_number, temperature in request_readings.items():
            logger.debug("Temperature reading: %s => %f" % (serial_number, temperature))
            try:
                # attempt to find sensor based on serial number (case insensitive)
                sensor = Sensor.get_sensor(serial_number)
                user_agent = self._get_user_agent(request)
                reading = Reading.create_temperature_reading(sensor, temperature, user_agent, save=True)
                logger.debug("Created temperature reading with ID %d" % reading.id)
            except Sensor.DoesNotExist:
                logger.error("Sensor with serial number '%s' does not exist", serial_number)

        # return empty response with HTTP 200 status code
        return Response()

    @staticmethod
    def _get_user_agent(request):
        user_agent_string = request.META.get('HTTP_USER_AGENT', None)
        if not user_agent_string:
            return None
        user_agent, created = UserAgent.objects.get_or_create(user_agent_string=user_agent_string)
        return user_agent
