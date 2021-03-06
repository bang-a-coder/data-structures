import math

def getParentKey(i):
	return math.floor((i-1)/2)

def getRightKey(i):
	return 2*i+2

def getLeftKey(i):
	return 2*i + 1

def isMaxHeap(arr):
	for i in range(len(arr)-1,0,-1):
		if arr[getParentKey(i)] < arr[i]:
			return False
	
	return True

sample = [10,6,7,5,15,17,12] #xomplete tree
sample2 = [7,6,10]
sample3 = [10,6,7,5,15,17,12,6,3,16] #incomplete tree


def maxHeapify(arr, i, heapSize = None): #maintain max heap property
	# print(arr, i)
	print(heapSize)
	le = getLeftKey(i)	
	ri = getRightKey(i)
	
	if heapSize == None:
		heapSize = len(arr) - 1
	
	if le <= heapSize and arr[le] > arr[i]:
		larger = le
	else:
		larger = i
	
	if ri <= heapSize and arr[ri] > arr[larger]:
		larger = ri
	
	# print(larger, i)
	if larger != i:
		smaller = arr[i]
		arr[i] = arr[larger]
		arr[larger] = smaller
		maxHeapify(arr, larger, heapSize)


# maxHeapify(sample3,0)
# print(sample3)

def buildMaxHeap(arr):
	for i in range(math.floor(len(arr)/2), -1, -1):
		maxHeapify(arr,i)

def heapSort(arr):
	buildMaxHeap(arr)
	heapSize = len(arr)-1
	for i in range(len(arr)-1,-1,-1):
		# print(len(arr), i)	
		root = arr[0]
		arr[0] = arr[i]
		arr[i] = root
		heapSize = heapSize -1
		maxHeapify(arr,0, heapSize)

		
# buildMaxHeap(sample3)
# print(sample3, isMaxHeap(sample3))
		
heapSort(sample3)
print(sample3)
		





















