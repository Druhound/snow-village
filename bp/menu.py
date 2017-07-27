# -*- coding: utf-8 -*-    verbose_name = "Магазин билетов"

from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from admin_tools.menu import items, Menu


class CustomMenu(Menu):
    """
    Custom Menu for attek admin site.
    """
    def __init__(self, **kwargs):
        Menu.__init__(self, **kwargs)
        self.children += [
            items.MenuItem(_('Dashboard'), reverse('admin:index')),
            items.Bookmarks('Закладки',
                            children=[
                                items.MenuItem('Пример 1', '#'),
                                items.MenuItem('Пример 2', '#'),
                            ]
            ),
            items.AppList(
                _('Applications'),
                exclude=('django.contrib.*',)
            ),
            items.AppList(
                _('Administration'),
                models=('django.contrib.*',)
            )
        ]

    def init_with_context(self, context):
        """
        Use this method if you need to access the request context.
        """
        return super(CustomMenu, self).init_with_context(context)

    class Media:
        css = {'all': ('css/admin_tools/custom_menu.css',)}