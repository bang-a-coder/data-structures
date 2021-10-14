import math

def getParentKey(i):
	return math.floor((i-1)/2)

def getRightKey(i):
	return 2*(i+1)

def getLeftKey(i):
	return 2*i + 1

def isMaxHeap(arr):
	for i in range(len(arr)-1,0,-1):
		if arr[getParentKey(i)] < arr[i]:
			return False
	
	return True

arr1 = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
arr2 = [24, 23, 22, 12, 21, 20, 8, 11, 10, 18, 16, 5]
arr3 = [23,17,14,6,13,10,1,5,7,12]
arr4 = [6,5,7]
arr4 = [6,4,7,5,3,0,1]
arr5 = [6,4,7,5,3,0,7]

def maxHeapify(A,i):
	print(A,i)
	le = getLeftKey(i)
	ri = getRightKey(i)
	
	heapSize = len(A) #Algo says that this should be the same but WTF it works for now
	
	print(le, i)
	if le <= heapSize and A[le] > A[i]:
		largest = le
	else:
		largest = i 
	
	if ri <= heapSize and A[ri] > A[i]:
		largest = ri

	if largest != i:
		smaller = A[i]
		A[i] = A[largest]
		A[largest] = smaller
		maxHeapify(A,largest-1)
	
	return A

print(maxHeapify(arr5, 0))

# print(isMaxHeap(arr1))
# print(isMaxHeap(arr2))
# print(isMaxHeap(arr3))

# print(getRightKey(0), 'should be 2')
# print(getRightKey(3), 'should be 8')

# print(getLeftKey(0), 'should be 1')
# print(getLeftKey(3), 'should be 7')

