from django.contrib import admin
from .models import client_data,company,services,Locations

admin.site.register(client_data)
admin.site.register(company)
admin.site.register(services)
admin.site.register(Locations)



