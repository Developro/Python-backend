from django.contrib import admin

# Register your models here.

from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from .models import User

#admin.site.register(User, UserAdmin)

#admin.site.unregister(Group)
