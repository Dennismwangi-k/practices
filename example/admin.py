from django.contrib import admin

# Register your models here.
from .models import Servers, ServerTypes

admin.site.register(Servers)
admin.site.register(ServerTypes)
