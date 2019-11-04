from functools import wraps
from SupportClasses import POSTClient
import datetime

pc = POSTClient.POSTClient()

def insert_bug_record(details, args, kwargs, source, dateCreated, status, expectedResolution):
        message=f'''INSERT INTO bugs (bugDetails, bugArguments, bugSource, bugDateCreated, bugStatus, bugExpectedResolution)
        VALUES ("{details}", "args: {args} kwargs: {kwargs}", "{source}", "{dateCreated}", "{status}", "{expectedResolution}")
        '''
        return(pc.send(message))


def my_logger(func):
	import logging
	logging.basicConfig(filename='{}.log'.format(func.__name__), level=logging.INFO)
	@wraps(func)
	def wrapper(*args, **kwargs):
		info_message='Ran with args: {}, and kwargs {}'.format(args, kwargs)
		logging.info("#####################################")
		logging.info(info_message)
		try:
			return(func(*args, **kwargs))
		except Exception as e:
			logging.info(e)
			logging.info("#####################################")
			
			details = e
			source = func.__name__
			dateCreated = datetime.datetime.now()
			status = "NEW"
			expectedResolution = "TBD"
			insert_bug_record(details, args, kwargs, source, dateCreated, status, expectedResolution)
			return("Exception Thrown")

	return wrapper