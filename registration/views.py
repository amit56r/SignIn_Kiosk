from django.shortcuts import render,redirect
from select_appointment.models import Patient, Doctor, Appointment
import datetime, requests

from .forms import BasicInfoForm,DetailForm

# Create your views here.







def register_screen(request, a_id):
	
	a_object =  Appointment.objects.get(a_id = a_id)
	return redirect('basic_info', a_id)



def basic_info(request, a_id):
	a_object =  Appointment.objects.get(a_id = a_id)

	if request.method == 'POST':
		form = BasicInfoForm(request.POST, instance = a_object.patient)
		if form.is_valid():
			form.save(commit=False)
			return  redirect( 'details', a_id)

	else:
		form = BasicInfoForm(instance = a_object.patient)


	return render(request,'registration/form.html',{'form' : form , 'a_obj' : a_object})


def details(request, a_id):
	a_object =  Appointment.objects.get(a_id = a_id)

	if request.method == 'POST':
		form = DetailForm(request.POST, instance = a_object)
		if form.is_valid():
			form.save(commit=False)
			return redirect( 'details', a_id)
	else:
		form = DetailForm(instance = a_object)


	return render(request,'registration/form.html',{'form' : form , 'a_obj' : a_object})
