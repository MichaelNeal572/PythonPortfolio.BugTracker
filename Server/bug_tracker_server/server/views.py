from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import sqlite3

conn = sqlite3.connect('employee.db')

c = conn.cursor()

@csrf_exempt
def home(request):
	if request.method =="POST":
		print(request.POST)
		return HttpResponse('Test')

def create_table_bugs(request):
	pass

def drop_table_bugs(request):
	pass

def create_table_devs(request):
	pass

def drop_table_devs(request):
	pass

def create_table_listeners(request):
	pass

def drop_table_listeners(request):
	pass

def create_table_backups(request):
	pass

def drop_table_backups(request):
	pass


