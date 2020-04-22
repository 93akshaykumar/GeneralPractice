array=[1,2,3,4,5,6,7,8,9]
find=10
def binarySearch(start,end):
	if start > end:
		return False
	mid=(start+end)//2
	if array[mid]==find: return True
	elif array[mid]>find: return binarySearch(0,mid-1) 
	elif array[mid]<find: return binarySearch(mid+1,end)
	else: return False

print("The element Found ==",binarySearch(0,len(array)-1))
