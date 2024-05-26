"""App Configuration"""

# Django
# AA example App
from django.apps import AppConfig

from base_plugin import __version__


class ExampleConfig(AppConfig):
    """App Config"""

    name = "base_plugin"
    label = "base_plugin"
    verbose_name = f"base_plugin App v{__version__}"
