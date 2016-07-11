from __future__ import unicode_literals

from django.utils import timezone
from django.db import models

# Create your models here.


class Patient(models.Model):
	p_id = models.IntegerField(blank=True)
	first_name  = models.CharField(max_length = 20)
	middle_name  =  models.CharField(max_length = 20, blank=True, null=True)
	last_name  = models.CharField(max_length = 20)
	date_of_birth = models.DateField(blank=True, null=True)

	MALE = 'Male'
	FEMALE ='Female'
	OTHER = 'Other'
	gender_list = [
					(MALE,MALE),
					(FEMALE,FEMALE),
					(OTHER,OTHER),
					]

	gender = models.CharField(max_length = 15,choices = gender_list, blank=True, null=True)
	address = models.CharField(max_length = 200, blank=True, null=True)
	city = models.CharField(max_length = 50, blank = True, null=True)
	state = models.CharField(max_length = 2,blank=True, null=True)
	zip_code = models.CharField(max_length=6, blank=True, null=True)


	cell_phone = models.CharField(max_length = 15, blank=True, null=True)
	home_phone = models.CharField(max_length =15,blank=True, null=True)

	email = models.CharField(max_length = 50, blank=True, null=True)

	emergency_contact_name = models.CharField(max_length = 50,blank=True, null=True)
	emergency_contact_phone = models.CharField(max_length = 50,blank=True, null=True)
	emergency_contact_relation = models.CharField(max_length = 50,blank=True, null=True)

	BLANK = 'blank'
	HISPANIC = 'hispanic'
	NOT_HISPANIC = 'not_hispanic'
	DECLINED = 'declined'
	ethnicity_list = [
						(BLANK, "Blank"),
						(HISPANIC,'Hispanic'),
						(NOT_HISPANIC, 'Not Hispanic'),
						(DECLINED,'Decline'),
						]

	ethnicity = models.CharField(max_length = 15, choices = ethnicity_list, default = BLANK, null=True)

	INDIAN = 'indian'
	ASIAN = 'asian'
	BLACK = 'black'
	HAWAIIAN = 'hawaiian'
	WHITE  = 'white'
	race_list = [
				(BLANK,'Blank'),
				(INDIAN, 'Indian'),
				(ASIAN, 'Asian'),
				(BLACK, 'Black'),
				(HAWAIIAN, 'Hawaiian'),
				(WHITE, 'White'),
				(DECLINED, 'Decline'),
			]

	race = models.CharField(max_length = 15, choices = race_list, default = BLANK, null=True)
	social_security_number = models.CharField(max_length = 15, blank=True, null=True)

	employer = models.CharField(max_length = 50, blank=True)
	employer_address = models.CharField(max_length = 200, blank=True, null=True)
	employer_city = models.CharField(max_length = 50, blank=True, null=True)
	employer_state = models.CharField(max_length = 2, blank=True, null=True)
	employer_zip_code = models.CharField(max_length = 6, blank=True, null=True)


	responsible_party_name = models.CharField(max_length = 50, blank=True, null=True)
	responsible_party_relation = models.CharField(max_length = 50, blank=True, null=True)
	responsible_party_phone = models.CharField(max_length = 15, blank=True, null=True)
	responsible_party_email = models.CharField(max_length = 50, blank=True, null=True)



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
	notes = models.TextField(blank=True)

	ARRIVED = 'Arrived'
	CANCELLED = 'Cancelled'
	COMPLETE = 'Complete'
	CONFIRMED  = 'Confirmed'
	IN_SESSION = 'In Session'
	NO_SHOW = 'No Show'
	NOT_CONFIRMED = 'Not Confirmed'
	RESCHEDULED  = 'Rescheduled'
	NONE = ''

	status_type = [
					(ARRIVED,ARRIVED),
					(CANCELLED,CANCELLED),
					(COMPLETE,COMPLETE),
					(CONFIRMED, CONFIRMED),
					(IN_SESSION, IN_SESSION),
					(NO_SHOW,NO_SHOW),
					(NOT_CONFIRMED, NOT_CONFIRMED),
					(RESCHEDULED, RESCHEDULED),
					(NONE,NONE),
					]

	status = models.CharField(blank=True, choices = status_type, default  = NONE, max_length = 10, null=True)


	def __str__(self):
		return '{} {}'.format(self.patient.first_name, self.scheduled_time)












