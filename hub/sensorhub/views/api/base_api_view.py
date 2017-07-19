from abc import ABCMeta
from rest_framework.views import APIView
from rest_framework import permissions


class BaseApiView(APIView, metaclass=ABCMeta):
    """
    Base API view class (no authentication).

    Documentation for Django REST framework class based views:
    http://www.django-rest-framework.org/api-guide/views/
    """

    # permissions: http://www.django-rest-framework.org/api-guide/permissions/
    permission_classes = (permissions.AllowAny,)
