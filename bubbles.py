def bubbleSort(A):
	for i in range(0,len(A)-1):
		for j in range(len(A)-1, i, -1):
			if A[j]<A[j-1]:
				smaller = A[j]
				A[j] = A[j-1]
				A[j-1] = smaller
				print(i, j, A)
	
	return A

arr = [5,3,2,4,1]

print(bubbleSort(arr))
