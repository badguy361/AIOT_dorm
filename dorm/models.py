from django.db import models

# Create your models here.
class facilities(models.Model):
	Date = models.IntegerField()
	facilities_name = models.CharField(max_length = 20)
	facilities_info = models.CharField(max_length = 10)
	facilities_voltage = models.FloatField()
	def __str__(self):
		return self.facilities_name