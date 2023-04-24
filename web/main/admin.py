from django.contrib import admin
from main.models import Servers

class ServersAdmin(admin.ModelAdmin):
    pass


admin.site.register(Servers, ServersAdmin)