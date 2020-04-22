print("Please Enter The elements in 1d array.Press '* to stop'")
value=''
array=[]
while value!='*':
	array2d=[]
	while value!='*':
		if value!='': array2d.append(value)
		value=input('Please Enter the number or "*"::')
	array.append(array2d)
	value=input('Please Enter the number or "*"::')

print(array[1].index('1'))
array.sort()
for element in array:
	element.sort()
array[1].pop(1)
#array[1].remove('4')
array.insert(0,100)
array[1].insert(0,200)
print(array)
print(len(array))
print(len(array[1]))
	
