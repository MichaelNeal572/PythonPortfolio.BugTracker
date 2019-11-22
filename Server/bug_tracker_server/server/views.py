from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import sqlite3
import json



@csrf_exempt
def home(request):
	if request.method =="POST":
		return HttpResponse('Test')

##CREATE/DROP STATEMENTS##
@csrf_exempt
def create_tables(request):
	if request.method =="POST":
		conn = sqlite3.connect('bugtracker.db')
		c = conn.cursor()
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
						devEmail text NOT NULL,
						devPassword text NOT NULL
					)
					''')
				c.execute('''
					CREATE TABLE listeners(
						devUserName text REFERENCES devs(devUserName),
						bugSource text REFERENCES bugs(bugSource)
					)
					''')
				c.execute('''
					CREATE TABLE backupListeners(
						backupDev text REFERENCES devs(devUserName) NOT NULL,
						dev text REFERENCES devs(devUserName) NOT NULL
					)
					''')
				c.execute('''INSERT INTO devs 
		    		(devUserName, devFirstName, devLastName, devPassword) 
		    		VALUES 
		    		(:devUserName, :devFirstName, :devLastName, :devPassword)''', 
		    		{"devUserName":"test", "devFirstName":"test", 
		    		"devLastName":"test", "devPassword":"test"})

		except Exception as e:
			return HttpResponse(str(e))
		else:
			return HttpResponse('Success')


@csrf_exempt
def drop_tables(request):
	if request.method =="POST":
		conn = sqlite3.connect('bugtracker.db')
		c = conn.cursor()
		try:
			with conn:
				c.execute("DROP TABLE bugs")
				c.execute("DROP TABLE devs")
				c.execute("DROP TABLE listeners")
				c.execute("DROP TABLE backupListeners")
		except Exception as e:
			return HttpResponse(str(e))
		else:
			return HttpResponse('Success')

@csrf_exempt
def get_bug_records(request):
	if request.method =="POST":
	    conn = sqlite3.connect('bugtracker.db')
	    c = conn.cursor()
	    response = {
	    "status":"Success",
	    "result":""
	    }
	    try:
	    	with conn:
		    	c.execute("SELECT rowId, bugDetails, bugArguments, bugSource, bugDateCreated, bugStatus, bugExpectedResolution FROM bugs")
		    	response["result"]=c.fetchall()
		    	print(response["result"])
	    except Exception as e:
	    	response["status"]="Error"
	    	response["result"]=str(e)
	    finally:
	    	return HttpResponse(json.dumps(response))

@csrf_exempt
def get_admin_records(request):
	if request.method =="POST":
	    conn = sqlite3.connect('bugtracker.db')
	    c = conn.cursor()
	    response = {
	    "status":"Success",
	    "result":""
	    }
	    try:
	    	with conn:
		    	c.execute("SELECT rowId, devUserName, devFirstName, devLastName, devPassword FROM devs")
		    	response["result"]=c.fetchall()
		    	print(response["result"])
	    except Exception as e:
	    	response["status"]="Error"
	    	response["result"]=str(e)
	    finally:
	    	return HttpResponse(json.dumps(response))

@csrf_exempt
def get_listener_records(request):
	if request.method =="POST":    
	    conn = sqlite3.connect('bugtracker.db')
	    c = conn.cursor()
	    response = {
	    "status":"Success",
	    "result":""
	    }
	    try:
	    	with conn:
		    	c.execute("SELECT rowId, devUserName, bugSource FROM listeners")
		    	response["result"]=c.fetchall()
		    	print(response["result"])
	    except Exception as e:
	    	response["status"]="Error"
	    	response["result"]=str(e)
	    finally:
	    	return HttpResponse(json.dumps(response))

@csrf_exempt
def get_backup_records(request):
	if request.method =="POST":
	    conn = sqlite3.connect('bugtracker.db')
	    c = conn.cursor()
	    response = {
	    "status":"Success",
	    "result":""
	    }
	    try:
	    	with conn:
		    	c.execute("SELECT rowId, backupDev, dev FROM backupListeners")
		    	response["result"]=c.fetchall()
		    	print(response["result"])
	    except Exception as e:
	    	response["status"]="Error"
	    	response["result"]=str(e)
	    finally:
	    	return HttpResponse(json.dumps(response))

#Insert##
@csrf_exempt
def insert_bug_record(request):
	if request.method =="POST":
	    conn = sqlite3.connect('bugtracker.db')
	    c = conn.cursor()
	    response = {
	    "status":"Success",
	    "result":""
	    }
	    try:
	    	with conn:
		    	c.execute('''INSERT INTO bugs 
		    		(bugDetails, bugArguments, bugSource, bugDateCreated, bugStatus, bugExpectedResolution) 
		    		VALUES 
		    		(:bugDetails, :bugArguments, :bugSource, :bugDateCreated, :bugStatus, :bugExpectedResolution)''', 
		    		{"bugDetails":request.POST["bugDetails"], "bugArguments":request.POST["bugArguments"], "bugSource":request.POST["bugSource"], 
		    		"bugDateCreated":request.POST["bugDateCreated"], "bugStatus":request.POST["bugStatus"], "bugExpectedResolution":request.POST["bugExpectedResolution"]})
	    except Exception as e:
	    	response["status"]="Error"
	    	response["result"]=str(e)
	    finally:
	    	return HttpResponse(json.dumps(response))

@csrf_exempt
def insert_admin_record(request):
	if request.method =="POST":
	    conn = sqlite3.connect('bugtracker.db')
	    c = conn.cursor()
	    response = {
	    "status":"Success",
	    "result":""
	    }
	    try:
	    	with conn:
		    	c.execute('''INSERT INTO devs 
		    		(devUserName, devFirstName, devLastName, devPassword) 
		    		VALUES 
		    		(:devUserName, :devFirstName, :devLastName, :devPassword)''', 
		    		{"devUserName":request.POST["devUserName"], "devFirstName":request.POST["devFirstName"], 
		    		"devLastName":request.POST["devLastName"], "devPassword":request.POST["devPassword"]})
	    except Exception as e:
	    	response["status"]="Error"
	    	response["result"]=str(e)
	    finally:
	    	return HttpResponse(json.dumps(response))


@csrf_exempt
def insert_listener_record(request):
	if request.method =="POST":
	    conn = sqlite3.connect('bugtracker.db')
	    c = conn.cursor()
	    response = {
	    "status":"Success",
	    "result":""
	    }
	    try:
	    	with conn:
		    	c.execute('''INSERT INTO listeners 
		    		(devUserName, bugSource) 
		    		VALUES 
		    		(:devUserName, :bugSource)''', 
		    		{"devUserName":request.POST["devUserName"], "bugSource":request.POST["bugSource"]})
	    except Exception as e:
	    	response["status"]="Error"
	    	response["result"]=str(e)
	    finally:
	    	return HttpResponse(json.dumps(response))

@csrf_exempt
def insert_backup_record(request):
	if request.method =="POST":
	    conn = sqlite3.connect('bugtracker.db')
	    c = conn.cursor()
	    response = {
	    "status":"Success",
	    "result":""
	    }
	    try:
	    	with conn:
		    	c.execute('''INSERT INTO backupListeners
		    		(backupDev, dev)
		    		VALUES 
		    		(:backupDev, :dev)''', 
		    		{"backupDev":request.POST["backupDev"], "dev":request.POST["dev"]})
	    except Exception as e:
	    	response["status"]="Error"
	    	response["result"]=str(e)
	    finally:
	    	return HttpResponse(json.dumps(response))

##Update##
@csrf_exempt
def update_bug_record(request):
    if request.method =="POST":
	    conn = sqlite3.connect('bugtracker.db')
	    c = conn.cursor()
	    response = {
	    "status":"Success",
	    "result":""
	    }
	    try:
	    	with conn:
		    	c.execute('''UPDATE bugs SET
		    		bugDetails = :details, 
				    bugArguments = :arguments, 
				    bugSource = :source", 
				    bugDateCreated = :dateCreated", 
				    bugStatus = :status", 
				    bugExpectedResolution = :expectedResolution"
				    WHERE rowid = :rowID
		    		''', 
		    		{"details":request.POST["details"],
		    		"arguments":f"args: {request.POST['args']} kwargs: {request.POST['kwargs']}",
		    		"source":request.POST["source"],
		    		"dateCreated":request.POST["dateCreated"],
		    		"status":request.POST["status"],
		    		"expectedResolution":request.POST["expectedResolution"],
		    		"rowID":request.POST["rowID"]})
	    except Exception as e:
	    	response["status"]="Error"
	    	response["result"]=str(e)
	    finally:
	    	return HttpResponse(json.dumps(response))

@csrf_exempt
def update_admin_record(request):
    if request.method =="POST":
	    conn = sqlite3.connect('bugtracker.db')
	    c = conn.cursor()
	    response = {
	    "status":"Success",
	    "result":""
	    }
	    try:
	    	with conn:
		    	c.execute('''UPDATE devs SET
		    		devUserName = :username, 
				    devFirstName = :firstname, 
				    devLastName = :lastname, 
				    devPassword = :password,
				    WHERE rowid = :rowID
		    		''', 
		    		{"username":request.POST["username"],
		    		"firstname":request.POST["firstname"],
		    		"lastname":request.POST["lastname"],
		    		"password":request.POST["password"],
		    		"rowID":request.POST["rowID"]})
	    except Exception as e:
	    	response["status"]="Error"
	    	response["result"]=str(e)
	    finally:
	    	return HttpResponse(json.dumps(response))

@csrf_exempt
def update_listener_record(request):
    if request.method =="POST":
	    conn = sqlite3.connect('bugtracker.db')
	    c = conn.cursor()
	    response = {
	    "status":"Success",
	    "result":""
	    }
	    try:
	    	with conn:
		    	c.execute('''UPDATE listeners SET
		    		devUserName = :username, 
				    bugSource = :source, 
				    WHERE rowid = :rowID
		    		''', 
		    		{"username":request.POST["username"],
		    		"source":request.POST["source"],
		    		"rowID":request.POST["rowID"]})
	    except Exception as e:
	    	response["status"]="Error"
	    	response["result"]=str(e)
	    finally:
	    	return HttpResponse(json.dumps(response))

@csrf_exempt
def update_backup_record(request):
    def update_listener_record(request):
	    if request.method =="POST":
		    conn = sqlite3.connect('bugtracker.db')
		    c = conn.cursor()
		    response = {
		    "status":"Success",
		    "result":""
		    }
		    try:
		    	with conn:
			    	c.execute('''UPDATE backupListeners SET
			    		backupDev = :backupDev, 
					    dev = :dev, 
					    WHERE rowid = :rowID
			    		''', 
			    		{"backupDev":request.POST["backupDev"],
			    		"dev":request.POST["dev"],
			    		"rowID":request.POST["rowID"]})
		    except Exception as e:
		    	response["status"]="Error"
		    	response["result"]=str(e)
		    finally:
		    	return HttpResponse(json.dumps(response))

##Delete##
@csrf_exempt
def delete_bug_record(request):
    if request.method =="POST":
	    conn = sqlite3.connect('bugtracker.db')
	    c = conn.cursor()
	    response = {
	    "status":"Success",
	    "result":""
	    }
	    try:
	    	with conn:
		    	c.execute('''DELETE FROM bugs 
				    WHERE rowid = :rowID
		    		''', 
		    		{"rowID":request.POST["rowID"]})
		    	response["result"]=c.fetchall()
		    	print(response["result"])
	    except Exception as e:
	    	response["status"]="Error"
	    	response["result"]=str(e)
	    finally:
	    	return HttpResponse(json.dumps(response))

@csrf_exempt
def delete_dev_record(request):
    if request.method =="POST":
	    conn = sqlite3.connect('bugtracker.db')
	    c = conn.cursor()
	    response = {
	    "status":"Success",
	    "result":""
	    }
	    try:
	    	with conn:
		    	c.execute('''DELETE FROM devs 
				    WHERE rowid = :rowID
		    		''', 
		    		{"rowID":request.POST["rowID"]})
		    	response["result"]=c.fetchall()
		    	print(response["result"])
	    except Exception as e:
	    	response["status"]="Error"
	    	response["result"]=str(e)
	    finally:
	    	return HttpResponse(json.dumps(response))

@csrf_exempt
def delete_listener_record(request):
    if request.method =="POST":
	    conn = sqlite3.connect('bugtracker.db')
	    c = conn.cursor()
	    response = {
	    "status":"Success",
	    "result":""
	    }
	    try:
	    	with conn:
		    	c.execute('''DELETE FROM listners 
				    WHERE rowid = :rowID
		    		''', 
		    		{"rowID":request.POST["rowID"]})
		    	response["result"]=c.fetchall()
		    	print(response["result"])
	    except Exception as e:
	    	response["status"]="Error"
	    	response["result"]=str(e)
	    finally:
	    	return HttpResponse(json.dumps(response))

@csrf_exempt
def delete_backup_record(request):
    if request.method =="POST":
	    conn = sqlite3.connect('bugtracker.db')
	    c = conn.cursor()
	    response = {
	    "status":"Success",
	    "result":""
	    }
	    try:
	    	with conn:
		    	c.execute('''DELETE FROM backupListeners 
				    WHERE rowid = :rowID
		    		''', 
		    		{"rowID":request.POST["rowID"]})
		    	response["result"]=c.fetchall()
		    	print(response["result"])
	    except Exception as e:
	    	response["status"]="Error"
	    	response["result"]=str(e)
	    finally:
	    	return HttpResponse(json.dumps(response))

@csrf_exempt
def get_distinct_admins(request):
    if request.method =="POST":
	    conn = sqlite3.connect('bugtracker.db')
	    c = conn.cursor()
	    response = {
	    "status":"Success",
	    "result":""
	    }
	    try:
	    	with conn:
		    	c.execute("SELECT DISTINCT devUserName FROM devs")
		    	response["result"]=c.fetchall()
		    	print(response)
	    except Exception as e:
	    	response["status"]="Error"
	    	response["result"]=str(e)
	    finally:
	    	return HttpResponse(json.dumps(response))

@csrf_exempt
def get_distinct_bug_sources(request):
    if request.method =="POST":
	    conn = sqlite3.connect('bugtracker.db')
	    c = conn.cursor()
	    response = {
	    "status":"Success",
	    "result":""
	    }
	    try:
	    	with conn:
		    	c.execute("SELECT DISTINCT bugSource FROM bugs")
		    	response["result"]=c.fetchall()
		    	print(response)
	    except Exception as e:
	    	response["status"]="Error"
	    	response["result"]=str(e)
	    finally:
	    	return HttpResponse(json.dumps(response))

@csrf_exempt
def check_user_login(request):
    if request.method =="POST":
	    conn = sqlite3.connect('bugtracker.db')
	    c = conn.cursor()
	    response = {
	    "status":"Success",
	    "result":""
	    }
	    try:
	    	with conn:
		    	c.execute('''SELECT EXISTS(SELECT devUserName, devPassword FROM devs
    						WHERE devUserName=:username AND devPassword=:password) AS found''', 
		    		{"username":request.POST["username"], "password":request.POST["password"]})
		    	response["result"]=c.fetchall()[0][0]
		    	print(response)
	    except Exception as e:
	    	response["status"]="Error"
	    	response["result"]=str(e)
	    finally:
	    	return HttpResponse(json.dumps(response))