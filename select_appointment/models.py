from __future__ import unicode_literals

from django.utils import timezone
from django.db import models

# Create your models here.

# lets get the bare min done and that worry about the other feilds


#TODO : add the required data later
class Patient(models.Model):
	p_id = models.IntegerField(blank=True)
	first_name  = models.CharField(max_length = 20)
	middle_name  =  models.CharField(max_length = 20, blank=True, null=True)
	last_name  = models.CharField(max_length = 20)

	def __str__(self):
		return '{} {}'.format(self.first_name,self.last_name)


class Doctor(models.Model):
	d_id = models.IntegerField(blank=True)
	first_name = models.CharField(max_length = 20)
	last_name = models.CharField(max_length = 20)

	def __str__(self):
		return '{} {}'.format(self.first_name,self.last_name)



class Office(models.Model):
	o_id = models.IntegerField(blank=True)
	name = models.CharField(max_length = 50)

	def __str__(self):
		return self.name


class Appointment(models.Model):
	patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
	doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
	office = models.ForeignKey(Office,on_delete=models.CASCADE)
	scheduled_time = models.DateTimeField(default=timezone.now())
	a_id = models.IntegerField(blank=True)
	duration = models.IntegerField(blank=True)
	reason  = models.TextField(blank=True)

	def __str__(self):
		return '{} {}'.format(self.patient.first_name, self.scheduled_time)












