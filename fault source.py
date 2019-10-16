import faultLogger

@faultLogger.my_logger
def sampleMath(num):
		i=num/1
		return i

if __name__=="__main__":
	print(sampleMath(5))