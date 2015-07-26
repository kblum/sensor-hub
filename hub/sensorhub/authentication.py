import logging
from rest_framework.authentication import BasicAuthentication
from .models import Token
from rest_framework.exceptions import AuthenticationFailed


class ApiUser(object):
    def __init__(self, token):
        """
        :type token: Token
        """
        self.token = token

    @property
    def api_key(self):
        if not self.token:
            return None
        return self.token.api_key

    def is_authenticated(self):
        # method used by `rest_framework.permissions.IsAuthenticated` class
        return self.api_key is not None


class ApiBasicAuthentication(BasicAuthentication):
    """
    Basic authentication using API credentials.

    Custom authentication documentation:
    http://www.django-rest-framework.org/api-guide/authentication/#custom-authentication
    """

    log = logging.getLogger(__name__)

    def authenticate_credentials(self, api_key, api_secret):
        if not api_key or not api_secret:
            return None  # no credentials provided

        # attempt to load token for request credentials
        try:
            token = Token.objects.enabled().get(api_key=api_key, api_secret=api_secret)
        except Token.DoesNotExist:
            self.log.warning('Invalid API credentials')
            raise AuthenticationFailed('Invalid credentials')
        except Token.MultipleObjectsReturned:
            # safety check as multiple objects should not exist with the same API credentials
            self.log.warning('Multiple tokens matching API credentials')
            raise AuthenticationFailed('Invalid credentials')

        user = ApiUser(token)
        return user, None,
