from django.db import models
from . import TimestampedModel


class UserAgent(TimestampedModel):
    """
    Representation of HTTP user agent string from reading API request.
    Exists as a separate model for database normalisation.
    """

    user_agent_string = models.TextField(db_index=True, unique=True, null=False, blank=False)

    @staticmethod
    def get_or_create_user_agent(user_agent_string, save=False):
        if not user_agent_string:
            return None
        try:
            # attempt to load user agent from user agent string
            return UserAgent.objects.get(user_agent_string=user_agent_string)
        except UserAgent.DoesNotExist:
            # create new user agent
            user_agent = UserAgent(user_agent_string=user_agent_string)
            if save:
                user_agent.save()
            return user_agent

    def __str__(self):
        return self.user_agent_string
