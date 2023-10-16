from django.contrib import admin
from DRRapp.models import DRRdb
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class DRRdbV(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=('slID','action','startDate','endDate','month_year', "datesExcluded", "numberOfDays", "leadCount", "expectedDrr", "lastUpdatedDate", "lastUpdatedTime")
admin.site.register(DRRdb,DRRdbV)