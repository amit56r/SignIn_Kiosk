from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.http import QueryDict
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from .models import token 
from .routines import *

import datetime, pytz, requests



def front_page(request):
	''' front page for site '''

	# clear the db - in order to see the lates data from the api
	clear_db()

	if request.method == "POST":
		return redirect('sign_in')
	elif 'code' in request.GET:
		return sign_in(request)

	return render(request,'frontpage.html',{})



def help_page(request):
	''' View for the help page '''

	return render(request, 'help.html',{})


def sign_in(request):
	''' main front page for sign-in kiosk '''

	#check if have alread gotten code
	token_list  = token.objects.order_by('expire_timestamp') 
	if 'code' in request.GET:
		get_token(request.GET['code'],token_list)
	elif 'error' in request.GET:
		return render(request,'frontpage.html',{'error': error})
	elif not token_list or token_list[0].has_expired() :
		#check if we have a valid token in our database
		return api_access(request)

	t = token.objects.order_by('expire_timestamp')[0]
	headers = {
				'Authorization': '{} {}'.format(t.token_type,t.access_token),
				}
	params = {
			'date': '2016-07-06',
			}
	patients_url = 'https://drchrono.com//api/appointments'
	data = requests.get(patients_url, headers=headers, params=params).json()

	return redirect('select_screen')


def api_access(request):
	''' api sigin redirection '''

	data = {
			'redirect_uri':'http://127.0.0.1:8000/',
			'client_id' : 'Xn6OmexKPoMVKouUPkpAqnPWjuMZREYAXAZZ25ym',
			'client_secret' : 'PA3AnZVm3U2cXymAos3Z0hELOyMJyFgUXBmYWzS873LRzNMUF86rXPq7FvDoBSolV7x9ZMTtf3N6BQDZnDRVPF1JpKn1SXUjFfG4op7AZQraBuGteIMJZ3jgykiKIine',
			'response_type' : 'code', 
	}

	qdata = QueryDict(mutable=True)
	qdata.update(data)

	return redirect('https://drchrono.com/o/authorize/?'+ qdata.urlencode())






