from django.shortcuts import render,redirect
from select_appointment.models import Patient, Doctor, Appointment
import datetime, requests

from .forms import BasicInfoForm,DetailForm, NotesForm

from .routines import *

# Create your views here.




def register_screen(request, a_id):
	
	a_object =  Appointment.objects.get(a_id = a_id)
	a_object.status = Appointment.ARRIVED
	a_object.save()
	return redirect('basic_info', a_id)



def basic_info(request, a_id):
	a_object =  Appointment.objects.get(a_id = a_id)

	if request.method == 'POST':
		form = BasicInfoForm(request.POST, instance = a_object.patient)
		if form.is_valid():
			form.save()
			return  redirect( 'details', a_id)

	else:
		form = BasicInfoForm(instance = a_object.patient)

	context = {
				'form' : form,
				'a_obj' : a_object,
				'section_name': "Basic Info",
				'progress': str(get_progess(a_object)),
				}

	return render(request,'registration/form.html',context)


def details(request, a_id):
	a_object =  Appointment.objects.get(a_id = a_id)

	if request.method == 'POST':
		form = DetailForm(request.POST, instance = a_object.patient)
		if form.is_valid():
			form.save()
			return redirect( 'notes_and_comments', a_id)
	else:
		form = DetailForm(instance = a_object.patient)


	context = {
				'form' : form,
				'a_obj' : a_object,
				'section_name' : 'Details',
				'progress': str(get_progess(a_object)),
				}

	return render(request,'registration/form.html',context)


def notes_and_comments(request,a_id):
	a_object =  Appointment.objects.get(a_id = a_id)

	if request.method == 'POST':
		form = NotesForm(request.POST, instance = a_object)
		if form.is_valid():
			form.save()
			return redirect( 'summary', a_id)
	else:
		form = NotesForm(instance = a_object)


	context = {
				'form' : form,
				'a_obj' : a_object,
				'section_name' : 'Notes and Comments',
				'progress': str(get_progess(a_object)),
				}

	return render(request,'registration/form.html',context)


def summary(request, a_id):
	
	a_object =  Appointment.objects.get(a_id = a_id)

	missing_list = []
	all_items,done,missing = get_items_status(a_object)
	missing_list.extend(missing)

	all_items,done,missing = get_items_status(a_object.patient)
	missing_list.extend(missing)

	if request.method == "POST":
		submit_data(a_object)
		return redirect('done_screen', a_id)

	context = {
				'a_obj' : a_object,
				'section_name' : 'Summary',
				'missing_list' : filter_list(missing_list)
				}

	return render(request,'registration/summary.html', context)



def done_screen(request,a_id):

	a_object =  Appointment.objects.get(a_id = a_id)

	context = {
				'a_obj' : a_object,
				'section_name' : 'Success',
				}

	return render(request, 'registration/done_page.html', context)








