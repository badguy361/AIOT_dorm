from django.db import models

# Create your models here.
class facilities_firstfloor(models.Model):
	Date = models.CharField(max_length = 30)
	facilities_name = models.CharField(max_length = 20)
	facilities_useage = models.CharField(max_length = 10)
	battery = models.FloatField()
	Acce_X = models.FloatField()
	Acce_Y = models.FloatField()
	Acce_Z = models.FloatField()
	Acce = models.FloatField()
	Temp = models.FloatField()
	Current = models.FloatField()
	Voltage = models.FloatField()
	Power = models.FloatField()
	
	def __str__(self):
		return self.facilities_name
	
class facilities_secondfloor(models.Model):
	Date = models.CharField(max_length = 30)
	facilities_name = models.CharField(max_length = 20)
	facilities_useage = models.CharField(max_length = 10)
	battery = models.FloatField()
	Acce_X = models.FloatField()
	Acce_Y = models.FloatField()
	Acce_Z = models.FloatField()
	Acce = models.FloatField()
	Temp = models.FloatField()
	Current = models.FloatField()
	Voltage = models.FloatField()
	Power = models.FloatField()

	def __str__(self):
		return self.facilities_name
	
class facilities_thirdfloor(models.Model):
	Date = models.CharField(max_length = 30)
	facilities_name = models.CharField(max_length = 20)
	facilities_useage = models.CharField(max_length = 10)
	battery = models.FloatField()
	Acce_X = models.FloatField()
	Acce_Y = models.FloatField()
	Acce_Z = models.FloatField()
	Acce = models.FloatField()
	Temp = models.FloatField()
	Current = models.FloatField()
	Voltage = models.FloatField()
	Power = models.FloatField()

	def __str__(self):
		return self.facilities_name


class facilities_fourthfloor(models.Model):
	Date = models.CharField(max_length = 30)
	facilities_name = models.CharField(max_length = 20)
	facilities_useage = models.CharField(max_length = 10)
	battery = models.FloatField()
	Acce_X = models.FloatField()
	Acce_Y = models.FloatField()
	Acce_Z = models.FloatField()
	Acce = models.FloatField()
	Temp = models.FloatField()
	Current = models.FloatField()
	Voltage = models.FloatField()
	Power = models.FloatField()

	def __str__(self):
		return self.facilities_name

class facilities_fifthfloor(models.Model):
	Date = models.CharField(max_length = 30)
	facilities_name = models.CharField(max_length = 20)
	facilities_useage = models.CharField(max_length = 10)
	battery = models.FloatField()
	Acce_X = models.FloatField()
	Acce_Y = models.FloatField()
	Acce_Z = models.FloatField()
	Acce = models.FloatField()
	Temp = models.FloatField()
	Current = models.FloatField()
	Voltage = models.FloatField()
	Power = models.FloatField()

	def __str__(self):
		return self.facilities_name