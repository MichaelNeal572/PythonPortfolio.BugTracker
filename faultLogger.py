from functools import wraps

def my_logger(func):
	import logging
	logging.basicConfig(filename='{}.log'.format(func.__name__), level=logging.INFO)

	@wraps(func)
	def wrapper(*args, **kwargs):
		info_message='Ran with args: {}, and kwargs {}'.format(args, kwargs)
		logging.info(info_message)
		return(func(*args, **kwargs))
	return wrapper