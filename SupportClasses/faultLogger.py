from functools import wraps
from SupportClasses.mqttClient import Client

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
			client = Client()
			client.insert_bug(str(e), info_message, func.__name__)
			logging.info("#####################################")
			return(f"An error occured: {e}")
	return wrapper