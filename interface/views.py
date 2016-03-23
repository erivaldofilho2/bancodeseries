from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader

# Create your views here.
def home(request):
	return HttpResponse('HOME')

def login(request):
	template = loader.get_template('login.html')
	context = RequestContext(request,{'aluno':'Erivaldo'})
	return HttpResponse(template.render(context))
