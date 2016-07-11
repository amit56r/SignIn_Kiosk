from django import forms 
from select_appointment.models import Patient, Doctor, Appointment


class BasicInfoForm(forms.ModelForm):

	class Meta:
		model = Patient
		fields = (
				'first_name', 
				'middle_name' ,
				'last_name',
				'date_of_birth',
				'gender',
				'social_security_number',
				'address',
				'city',
				'state',
				'zip_code',
				'cell_phone',
				'home_phone',
				'email',
				'ethnicity',
				'race',
				)




class DetailForm(forms.ModelForm):

	class Meta:
		model  = Patient
		fields = (
					'emergency_contact_name',
					'emergency_contact_phone',
					'emergency_contact_relation',
					'employer',
					'employer_address',
					'employer_city',
					'employer_state',
					'employer_zip_code',
					'responsible_party_name',
					'responsible_party_relation',
					'responsible_party_phone',
					'responsible_party_email',
					)



class NotesForm(forms.ModelForm):
	
	class Meta:
		model = Appointment
		fields = (
					'reason', 
					'notes',
					)