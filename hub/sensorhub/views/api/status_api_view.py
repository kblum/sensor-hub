from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response


class StatusApiView(APIView):
    """
    View for status check API method.
    """

    permission_classes = (permissions.AllowAny,)

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def get(self, request):
        # return empty response with HTTP 200 status code
        return Response()
