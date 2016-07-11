from .models import Patient, Doctor, Appointment, Office
from SignIn_Kiosk.models import token
from django.utils import timezone
import datetime, pytz, requests
from django.core.exceptions import *




def import_data():
	''' routine to import data from api'''

	token_list  = token.objects.order_by('expire_timestamp') 
	assert(len(token_list) == 1)

	t = token_list[0]
	headers = {
				'Authorization': '{} {}'.format(t.token_type,t.access_token),
				}

	import_appointment(headers)



def add_patient(headers,p_id):

	patient_url = 'https://drchrono.com/api/patients/{}'.format(p_id)
	result = requests.get(patient_url,headers=headers).json()

	p  = Patient(
				p_id = result['id'],
				first_name = result['first_name'],
				middle_name = result['middle_name'],
				last_name = result['last_name'],
				date_of_birth = result['date_of_birth'],
				gender = result['gender'],
				address = result['address'],
				city  = result['city'],
				state = result['state'],
				zip_code = result['zip_code'],
				cell_phone = result['cell_phone'],
				home_phone = result['home_phone'],
				email = result['email'],
				emergency_contact_name = result['emergency_contact_name'],
				emergency_contact_phone = result['emergency_contact_phone'],
				emergency_contact_relation = result['emergency_contact_relation'],
				ethnicity = result['ethnicity'],
				race = result['race'],
				social_security_number = result['social_security_number'],
				employer = result['employer'],
				employer_address = result['employer_address'],
				employer_city = result['employer_city'],
				employer_state = result['employer_state'],
				employer_zip_code = result['employer_zip_code'],
				responsible_party_name = result['responsible_party_name'],
				responsible_party_relation = result['responsible_party_relation'],
				responsible_party_phone = result['responsible_party_phone'],
				responsible_party_email = result['responsible_party_email'],

					)
	p.save()
	return p


def add_doctor(headers,d_id):
	doctor_url = 'https://drchrono.com/api/doctors/{}'.format(d_id)
	result = requests.get(doctor_url,headers=headers).json()

	d = Doctor(
				d_id = result['id'],
				first_name = result['first_name'],
				last_name = result['last_name'],	
				)

	d.save()
	return d


def add_office(headers,o_id):
	office_url = 'https://drchrono.com/api/offices/{}'.format(o_id)
	result = requests.get(office_url,headers=headers).json()

	o = Office(
				o_id = result['id'],
				name = result['name'],

				)
	o.save()
	return o



def import_appointment(headers):
	appointment_url = 'https://drchrono.com/api/appointments'
	params = {
				'date': timezone.now().isoformat()[0:10]
	}
	
	results = []

	while appointment_url:
		data = requests.get(appointment_url ,headers = headers, params = params).json()
		results.extend(data['results'])
		appointment_url = data['next']
	

	# need to populate the database
	for a in results:


		p_id = a['patient']
		d_id  = a['doctor']
		o_id = a['office']
		a_id = a['id']


		try:
			p = Patient.objects.get(p_id = p_id)
		except ObjectDoesNotExist:
			p = add_patient(headers,p_id)

		try:
			d = Doctor.objects.get(d_id = d_id)
		except ObjectDoesNotExist:
			d = add_doctor(headers,d_id)


		try:
			o = Office.objects.get(o_id = o_id)
		except ObjectDoesNotExist:
			o = add_office(headers,o_id)


		try:
			a_object = Appointment.objects.get(a_id = a_id)
		except ObjectDoesNotExist:
			a_object =  Appointment(
								scheduled_time = a['scheduled_time'],
								a_id = a['id'],
								duration= a['duration'],
								reason = a['reason'],
								notes = a['notes'],
								patient = p,
								doctor = d,
								office = o,
								status  = a['status']
								)
		a_object.save()



	






