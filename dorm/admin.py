from django.contrib import admin
from dorm.models import facilities_firstfloor,facilities_secondfloor,\
        facilities_thirdfloor,facilities_fourthfloor,facilities_fifthfloor
# Register your models here.
admin.site.register(facilities_firstfloor)
admin.site.register(facilities_secondfloor)
admin.site.register(facilities_thirdfloor)
admin.site.register(facilities_fourthfloor)
admin.site.register(facilities_fifthfloor)