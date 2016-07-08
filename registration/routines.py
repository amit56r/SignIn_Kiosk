
from select_appointment.models import Patient, Doctor, Appointment
from SignIn_Kiosk.models import token
import datetime, requests



def submit_data(a_object):
	token_list  = token.objects.order_by('expire_timestamp') 
	assert(len(token_list) == 1)

	t = token_list[0]
	headers = {
				'Authorization': '{} {}'.format(t.token_type,t.access_token),
				}
	

	p = a_object.patient
	patient_url = 'https://drchrono.com/api/patients/{}'.format(p.p_id)

	data = {
			'first_name' : p.first_name,
			'middle_name' : p.middle_name,
			'last_name' : p.last_name,
			'date_of_birth' : p.date_of_birth,
			'gender' : p.gender,
			'address' : p.address,
			'city' : p.city,
			'state' : p.state,
			'zip_code' : p.zip_code,
			'cell_phone' : p.cell_phone,
			'home_phone' : p.home_phone,
			'email' : p.email,
			'emergency_contact_name' : p.emergency_contact_name,
			'emergency_contact_phone' : p.emergency_contact_phone,
			'emergency_contact_relation' : p.emergency_contact_relation,
			'ethnicity' : p.ethnicity,
			'race' : p.race,
			'social_security_number' : p.social_security_number,
			'employer' : p.employer,
			'employer_address' : p.employer_address,
			'employer_city' : p.employer_city,
			'employer_state' : p.employer_state,
			'employer_zip_code' : p.employer_zip_code,
			'responsible_party_name' : p.responsible_party_name,
			'responsible_party_relation' : p.responsible_party_relation,
			'responsible_party_phone' : p.responsible_party_phone,
			'responsible_party_email' : p.responsible_party_email,
		}

	reply = requests.patch(patient_url,headers = headers,data = data).json()


	a = a_object
	appointment_url = 'https://drchrono.com//api/appointments/{}'.format(a.a_id)

	data = {
			'reason': a.reason,
			'notes' : a.notes,
			'status': a.status
	}

	reply = requests.patch(appointment_url,headers = headers,data = data).json()
	#for key, value in reply.iteritems():
	#	print key, ' -> ', value



def get_items_status(model_object):
	done_items = []
	missing_items = []
	field_items = []

	#check pateint
	object_fields = model_object._meta.get_fields(include_parents=False)
	for field in object_fields:
		value = getattr(model_object, field.name, True)
		name =  model_object.__class__.__name__ +'_' + field.name
		#print field.name,value
		if value:
			done_items.append(name)
		else:
			missing_items.append(name)
		field_items.append(name)


	return field_items,done_items,missing_items



def get_progess(a_object):
	done_count = 0
	feild_count = 0

	all_items,done,missing = get_items_status(a_object)
	done_count += len(done)
	feild_count += len(all_items)


	all_items,done,missing = get_items_status(a_object.patient)
	done_count += len(done)
	feild_count += len(all_items)

	return (done_count*100)/(feild_count)



def filter_list(missing_list):
	for i,item in enumerate(missing_list):
		missing_list[i] = ' '.join([ x.capitalize() for x in item.split('_')[1:]])
	return missing_list



