from django.shortcuts import render
from SignIn_Kiosk.models import token
from .models import Patient, Doctor, Appointment

from .routines import import_data, clear_db

from django.shortcuts import redirect
from django.utils import timezone

from .forms import PatientForm
from  registration.views import * 

import datetime, requests


# Create your views here.





def select_screen(request):	
	clear_db()  #since appointment can be updated (also we are only gettin data for the day) - not expensive
	import_data() 

	#print request.POST

	if request.method == 'POST':
		form  = PatientForm(request.POST)
		if form.is_valid():
			p  = form.save(commit=False)
			return appointment_list(request,p)
	elif 'selection' in request.GET:
		#pass it onto the registration part
		return redirect('register_screen', a_id = request.GET['selection'])
	else:
		form  = PatientForm()


	return render(request, 'select_appointment/index.html', {'form': form})



def appointment_list(request, p):

	p_list  = Patient.objects.filter(last_name__iexact = p.last_name).filter(first_name__iexact = p.first_name)

	a_list = []
	now = timezone.now() - datetime.timedelta(minutes=30)
	for p in p_list:
		a_list.extend(Appointment.objects.filter(patient  = p).filter(scheduled_time__gte = now))

	
	#print p_list
	#print a_list


	return render(request, 'select_appointment/list.html', {'a_list': a_list})


