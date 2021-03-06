import logging
from . import BaseApiView
from rest_framework.response import Response

logger = logging.getLogger(__name__)


class StatusApiView(BaseApiView):
    """
    View for status check API method.
    """

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def get(self, request):
        logger.info("Status API check called")
        # return empty response with HTTP 200 status code
        return Response()
