print("Please Enter The elements in 1d array.Press '* to stop'")
value=input('Please Enter the number or "*"::')
array=[]
while value!='*':
	array.append(int(value))
	value=input('Please Enter the number or "*"::')
array.sort()
array.pop(1)
array.remove(6)
array.insert(0,100)
print(array)
print(len(array))

	
