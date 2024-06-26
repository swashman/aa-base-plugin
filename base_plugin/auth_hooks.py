"""Hook into Alliance Auth"""

# Django
# Alliance Auth
from django.utils.translation import gettext_lazy as _

from allianceauth import hooks
from allianceauth.services.hooks import MenuItemHook, UrlHook

# AA Example App
from base_plugin import urls


class ExampleMenuItem(MenuItemHook):
    """This class ensures only authorized users will see the menu entry"""

    def __init__(self):
        # setup menu entry for sidebar
        MenuItemHook.__init__(
            self,
            _("Base Plugin App"),
            "fas fa-cube fa-fw",
            "base_plugin:index",
            navactive=["base_plugin:"],
        )

    def render(self, request):
        """Render the menu item"""

        if request.user.has_perm("base_plugin.basic_access"):
            return MenuItemHook.render(self, request)

        return ""


@hooks.register("menu_item_hook")
def register_menu():
    """Register the menu item"""

    return ExampleMenuItem()


@hooks.register("url_hook")
def register_urls():
    """Register app urls"""

    return UrlHook(urls, "base_plugin", r"^base_plugin/")
