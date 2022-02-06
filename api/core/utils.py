import os

from django.core.exceptions import ImproperlyConfigured


# because get_env_value is called in setttings.py we cannot import
# from modules specified in INSTALLED_APPS in this file


def get_env_value(env_variable, default=None):
    """Get environment variable by name.

    Raise error when environment variable is missing and default value is not set.

    Arguments:
        env_variable: variable name
        default: default value
    Returns:
        Value taken from environment variable or default value
    """

    try:
        return os.environ[env_variable]
    except KeyError:
        if default is not None:
            return default
        else:
            raise ImproperlyConfigured(f"Set the {env_variable} environment variable")
