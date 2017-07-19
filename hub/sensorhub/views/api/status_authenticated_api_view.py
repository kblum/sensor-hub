import logging
from . import BaseAuthenticatedApiView
from rest_framework.response import Response

logger = logging.getLogger(__name__)


class StatusAuthenticatedApiView(BaseAuthenticatedApiView):
    """
    View for authenticated status check API method.
    """

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def get(self, request):
        logger.info("Authenticated status API check called")
        logger.error("BANK!")
        # return empty response with HTTP 200 status code
        return Response()
