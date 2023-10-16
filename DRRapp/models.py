from django.db import models

# Create your models here.
class DRRdb(models.Model):
    slID = models.AutoField(primary_key=True)
    action = models.CharField(blank=True, null=True, max_length=50)
    startDate = models.DateField()
    endDate = models.DateField()
    month_year = models.IntegerField()
    datesExcluded = models.TextField(blank=True, null=True)
    numberOfDays = models.IntegerField()
    leadCount = models.IntegerField()
    expectedDrr = models.IntegerField()
    lastUpdatedDate = models.DateField(auto_now=True)
    lastUpdatedTime = models.TimeField(auto_now=True)

    # def __str__(self):
    #     return self.slID