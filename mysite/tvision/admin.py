# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Auto
from .models import ReleasePage
from .models import BugPage

# Register your models here.
admin.site.register(Auto)
admin.site.register(ReleasePage)
admin.site.register(BugPage)
