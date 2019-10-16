from functools import wraps

def my_logger(func):
	import logging
	logging.basicConfig(filename='{}.log'.format(func.__name__), level=logging.INFO)

	@wraps(func)
	def wrapper(*args, **kwargs):
		logging.info('Ran with args: {}, and kwargs {}'.format(args, kwargs))
	return wrapper

@my_logger
def sampleMath():
		i=5/0
		return i

if __name__=="__main__":
	print(sampleMath())