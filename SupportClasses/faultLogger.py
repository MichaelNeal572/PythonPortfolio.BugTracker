from functools import wraps
from SupportClasses import POSTClient
import datetime

pc = POSTClient.POSTClient()

def insert_bug_record(details, args, kwargs, source, dateCreated, status, expectedResolution):
        message = {
            "details":details, 
            "args":args, 
            "kwargs":kwargs, 
            "source":source, 
            "dateCreated":dateCreated, 
            "status":status, 
            "expectedResolution":expectedResolution
        }
        return(self.pc.send(url = "insert-bug-record", message=message))


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
			dateCreated = datetime.date.today()
			status = "NEW"
			expectedResolution = "TBD"
			print(insert_bug_record(details, args, kwargs, source, dateCreated, status, expectedResolution))
			
			return("Exception Thrown")

	return wrapper