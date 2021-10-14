#WORKS ONLLY FOR ARRAYS OF LEN MULTIPLE OF 2

import math

def sort(arr):
	subLen = int(len(arr)/2)

	L = []
	R = []

	for l in range(0,subLen):
		L.append(arr[l])
	for r in range (subLen, len(arr)):
		R.append(arr[r])

	L.append(math.inf)
	R.append(math.inf)

	a = 0
	b = 0
	for k in range(0,len(arr)):
		if L[a] <= R[b]:
			arr[k] = L[a]
			a += 1
		else:
			arr[k] = R[b]
			b += 1
	
	return arr

def mergeSort(A):
	print(A)
	if len(A) == 2: return sort(A)

	return sort(mergeSort(A[:len(A)//2]) + mergeSort(A[len(A)//2:]))

arr = [54,26,93,17,77,1,44,55]
# mergeSort(A)
print(mergeSort(arr))
	