from django.shortcuts import render
from django.http import HttpResponse

test = [
	{
		'name':'mike',
		'surname':'neal'
	},
	{
		'name':'john',
		'surname':'doe'
	}
]

def home(request):
	return render(request, 'admin_dashboard/home.html')

def about(request):
	context = {
		'tests':test,
		'title':'About'
	}
	return render(request, 'admin_dashboard/about.html', context)
