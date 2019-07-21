from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Record)
admin.site.register(SeasonSchedule)
admin.site.register(ScheduleItem)
admin.site.register(Roster)
admin.site.register(StaffMember)
