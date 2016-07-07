from django import forms 
from select_appointment.models import Patient, Doctor, Appointment


class BasicInfoForm(forms.ModelForm):

	class Meta:
		model = Patient
		fields = ('first_name', 'middle_name' ,'last_name')




class DetailForm(forms.ModelForm):

	class Meta:
		model  = Appointment
		fields = ('duration', 'reason')