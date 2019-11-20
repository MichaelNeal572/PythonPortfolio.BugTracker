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

##CREATE/DROP STATEMENTS##
@csrf_exempt
def create_tables(request):
	try:
		with conn:
			c.execute('''
				CREATE TABLE bugs(
					bugDetails text NOT NULL,
					bugArguments text NOT NULL,
					bugSource text NOT NULL,
					bugDateCreated text NOT NULL,
					bugStatus text NOT NULL,
					bugExpectedResolution text NOT NULL
				)
				''')
			c.execute('''
				CREATE TABLE devs(
					devUserName text PRIMARY KEY NOT NULL,
					devFirstName text NOT NULL,
					devLastName text NOT NULL,
					devEmail text,
					devPassword text NOT NULL
				)
				''')
			c.execute('''
				CREATE TABLE listeners(
					devUserName int REFERENCES devs(devUserName),
					bugSource int REFERENCES bugs(bugSource)
				)
				''')
			c.execute('''
				CREATE TABLE backupListeners(
					backupDevID int REFERENCES devs(devUserName) NOT NULL,
					devID int REFERENCES devs(devUserName) NOT NULL
				)
				''')
	except Exception as e:
		return HttpResponse(str(e))
	else:
		return HttpResponse('Success')


@csrf_exempt
def drop_tables(request):
	with conn:



##########################

##INSERT##

##UPDATE##

##DELETE##

##READ##

##OTHER##



