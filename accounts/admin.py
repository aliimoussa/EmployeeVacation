from django.contrib import admin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from accounts.models import Account

admin.site.register(Account)