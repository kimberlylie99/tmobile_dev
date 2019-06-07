# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.admin import AdminSite

from .models import AutoPage
from .models import ReleasePage
from .models import BugPage

# Register your models here.
admin.site.register(AutoPage)
admin.site.register(ReleasePage)
admin.site.register(BugPage)

class PersonalAdmin(AdminSite):
    site_header = "T|Vision Adminstration"

admin_site = PersonalAdmin(name='myadmin')
admin_site.register(AutoPage)
admin_site.register(ReleasePage)
admin_site.register(BugPage)

# username: admin
# password: adminadmin
