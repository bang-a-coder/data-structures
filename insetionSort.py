def insertionSort(A):
	for j in range(1,len(A)):
		key = A[j]
		i = j - 1
		while i>=0 and A[i]>key:
			A[i+1] = A[i]
			i = i - 1
		A[i+1] = key
	
	return A

arr = [22,15,36,20,3]
# print(insertionSort(arr))

def reInsertion(A,n):
	if n<0: return 

	reInsertion(A, n-1)

	x = A[n]
	i = n - 1
	while i>=0 and A[i]>x:
		A[i+1] = A[i]
		i = i - 1
	A[i+1] = x
	print(A)
	return A

print(reInsertion(arr, 4))

# def fuckarray(arr):
# 	return arr.append('ti sto poutso')

# def test(arr):
# 	fuckarray(arr)

# 	print(arr)

# test(arr)
