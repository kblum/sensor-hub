import logging
from hub.sensorhub.authentication import ApiBasicAuthentication
from hub.sensorhub.models import Sensor, Reading
from rest_framework import permissions
from rest_framework.exceptions import ParseError
from rest_framework.views import APIView
from rest_framework.response import Response

logger = logging.getLogger(__name__)


class TemperatureApiView(APIView):
    """
    View for temperature API.
    Allows temperature readings to be recorded through POST requests.

    Documentation for Django REST framework class based views:
    http://www.django-rest-framework.org/api-guide/views/
    """

    # authentication: http://www.django-rest-framework.org/api-guide/authentication/
    authentication_classes = (ApiBasicAuthentication,)

    # permissions: http://www.django-rest-framework.org/api-guide/permissions/
    permission_classes = (permissions.IsAuthenticated,)

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
                sensor = Sensor.objects.enabled().get(serial_number=serial_number)
                reading = Reading.create_temperature_reading(sensor, temperature, save=True)
                logger.debug("Created temperature reading with ID %d" % reading.id)
            except Sensor.DoesNotExist:
                logger.error("Sensor with serial number '%s' does not exist", serial_number)

        # return empty response with HTTP 200 status code
        return Response()