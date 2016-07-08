from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.http import QueryDict
from django.core.urlresolvers import reverse


from django.contrib.auth.decorators import login_required

import datetime, pytz, requests

from .models import token 




def front_page(request):

	if request.method == "POST":
		return redirect('sign_in')
	elif 'code' in request.GET:
		return sign_in(request)


	return render(request,'frontpage.html',{})


def help_page(request):
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
		#assuming we are only catering to one user
		return api_access(request)


	t = token.objects.order_by('expire_timestamp')[0]
	#testing apit comminucation
	headers = {
				'Authorization': '{} {}'.format(t.token_type,t.access_token),
				}
	params = {
			'date': '2016-07-06',
	}
	patients_url = 'https://drchrono.com//api/appointments'
	data = requests.get(patients_url, headers=headers, params=params).json()

	# for d in data['results']:
	# 	for key, value in d.iteritems():
	# 		print key, value


	return redirect('select_screen')



def get_token(code,token_list):
	data_dict = {
		'code' : code,
		'grant_type' : 'authorization_code',
		'redirect_uri' : 'http://127.0.0.1:8000/',
		'client_id' : 'Xn6OmexKPoMVKouUPkpAqnPWjuMZREYAXAZZ25ym',
		'client_secret' : 'PA3AnZVm3U2cXymAos3Z0hELOyMJyFgUXBmYWzS873LRzNMUF86rXPq7FvDoBSolV7x9ZMTtf3N6BQDZnDRVPF1JpKn1SXUjFfG4op7AZQraBuGteIMJZ3jgykiKIine',
	}

	response = requests.post('https://drchrono.com/o/token/',data = data_dict)
	data = response.json()
	#print data


	#not handling refresh token
	if not  token_list:
		#we need to create and store a token
		new_token = token()
		new_token.access_token = data['access_token']
		new_token.refresh_token = data['refresh_token']
		time_holder = timezone.now() + datetime.timedelta(seconds=data['expires_in'])
		new_token.expire_timestamp = time_holder.isoformat()
		new_token.token_type = data['token_type']
		new_token.scope = data['scope']
		new_token.save()
	else:
		#update the expired token in the database
		curr_token = token_list[0]
		curr_token.access_token = data['access_token']
		curr_token.refresh_token = data['refresh_token']
		time_holder = timezone.now() + datetime.timedelta(seconds=data['expires_in'])
		curr_token.expire_timestamp = time_holder.isoformat()
		curr_token.token_type = data['token_type']
		curr_token.scope = data['scope']
		curr_token.save()






def api_access(request):
	print '###', request.build_absolute_uri(reverse('sign_in'))
	data = {
			'redirect_uri':'http://127.0.0.1:8000/',
			'client_id' : 'Xn6OmexKPoMVKouUPkpAqnPWjuMZREYAXAZZ25ym',
			'client_secret' : 'PA3AnZVm3U2cXymAos3Z0hELOyMJyFgUXBmYWzS873LRzNMUF86rXPq7FvDoBSolV7x9ZMTtf3N6BQDZnDRVPF1JpKn1SXUjFfG4op7AZQraBuGteIMJZ3jgykiKIine',
			'response_type' : 'code', 
	}

	qdata = QueryDict(mutable=True)
	qdata.update(data)

	return redirect('https://drchrono.com/o/authorize/?'+ qdata.urlencode())






