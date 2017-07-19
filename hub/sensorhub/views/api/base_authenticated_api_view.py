from abc import ABCMeta
from hub.sensorhub.authentication import ApiBasicAuthentication
from . import BaseApiView
from rest_framework import permissions


class BaseAuthenticatedApiView(BaseApiView, metaclass=ABCMeta):
    """
    Base API view class with authentication.
    """

    # authentication: http://www.django-rest-framework.org/api-guide/authentication/
    authentication_classes = (ApiBasicAuthentication,)

    # permissions: http://www.django-rest-framework.org/api-guide/permissions/
    permission_classes = (permissions.IsAuthenticated,)
