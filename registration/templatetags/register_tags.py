from django import template
from django.core.urlresolvers import reverse, resolve

register = template.Library()



@register.simple_tag
def isActive(request, page):
	#print page
	#print resolve(request.path).view_name
	if page == resolve(request.path).view_name:
		return 'class=active'
	else:
		return ''