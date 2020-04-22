def factorial(factValue):
	if factValue<=1: return 1
	else: return factValue * factorial(factValue-1)
try:
	factValue=int(input("Please Enter The Number To Find Factorial=="))
except:
	print("ERROR - Please Enter The Interger value")
else:	
	print("The Factorial of ",factValue," is== ",factorial(factValue))
