from SupportClasses.faultLogger import my_logger

@my_logger
def sampleMath(num):
		i=num/0
		return i

if __name__=="__main__":
	print(sampleMath(5))