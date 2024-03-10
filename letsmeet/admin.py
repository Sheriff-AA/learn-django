from django.contrib import admin
from .models import Linkup, Location, Attendee

# Register your models here.

class LinkupAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'date', 'location')
    list_filter = ('location', 'date')
    prepopulated_fields = {'slug': ('title', )}

admin.site.register(Linkup, LinkupAdmin) #sherif --qwerty+
admin.site.register(Location)
admin.site.register(Attendee)