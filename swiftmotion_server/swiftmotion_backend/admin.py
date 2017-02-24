from django.contrib import admin

from .models import BackInjury, RecordID, SensorEntry
# Register your models here.

admin.site.register(BackInjury)
admin.site.register(RecordID)
admin.site.register(SensorEntry)
