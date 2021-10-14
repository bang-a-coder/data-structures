arr = [22,15,36,20,3]

def selectionSort(A):
	for i in range(0, len(A)-1):
		print(A)
		m = i
		for j in range(i+1,len(A)):
			if A[j] < A[m]:
				m = j
		x = A[m]
		print(x)
		A[m] = A[i]
		A[i] = x

	return A


print(selectionSort(arr))