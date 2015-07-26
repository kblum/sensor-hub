import os
import binascii
from django.db import models
from . import TimestampedModel, EnabledQuerySet


class Token(TimestampedModel):
    """
    API credentials.
    """

    # length in number of hexadecimal characters (must be a multiple of 2)
    __api_key_length = 16
    __api_secret_length = 16

    name = models.CharField(max_length=64)
    api_key = models.CharField("API key", max_length=__api_key_length, null=False, editable=False, unique=True)
    api_secret = models.CharField("API secret", max_length=__api_secret_length, null=False, editable=False)
    enabled = models.BooleanField(default=True, db_index=True)

    objects = EnabledQuerySet.as_manager()

    def save(self, *args, **kwargs):
        """
        Randomly generate API key and secret for token when it is created.
        """
        if not self.id:
            self.api_key = self.__generate_key(self.__api_key_length)
            self.api_secret = self.__generate_key(self.__api_secret_length)
        super(Token, self).save(*args, **kwargs)

    @staticmethod
    def __generate_key(length):
        """
        Generate a random key.
        :param length: length of key in number of hexadecimal characters
        :return: key in hexadecimal format
        """
        if length % 2 != 0:
            raise ValueError("'length' must be a multiple of 2")
        length_bytes = int(length / 2)  # length of key in bytes
        key_bytes = os.urandom(length_bytes)
        return binascii.hexlify(key_bytes).decode()

    def __str__(self):
        return self.name

    class Meta(TimestampedModel.Meta):
        index_together = [
            ('api_key', 'api_secret',),
        ]
