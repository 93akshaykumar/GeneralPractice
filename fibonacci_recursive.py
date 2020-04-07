def fibonacci(fibValue):
	if fibValue==1: return 0
	elif fibValue==2: return 1
	else: return fibonacci(fibValue-1) + fibonacci(fibValue-2)
try:
	fibValue=int(input("Please Enter The Number To Find Fibonacci=="))
	if fibValue<=0: raise
except:
	print("ERROR - Please Enter The Interger value")
else:	
	print("The Fibonacci of ",fibValue," is== ",fibonacci(fibValue))
