# isGFG: , Link: 
# IsDone: 0
def TwoElementsClosestToZero(A):
	n = len(A)
	if(n < 2):
		print "Invalid Input"
		return
 	minLeft = 0
	minRight = 1
	minSum = A[0] + A[1]
	for l in range(1, n - 1):
		for r in range(l + 1, n):
			sum = A[l] + A[r];
			if(abs(minSum) > abs(sum)):
				minSum = sum
				minLeft = l
				minRight = r
	print " The two elements whose sum is minimum are ", A[minLeft], A[minRight]

A = [1, 60, -10, 70, -80, 85]
TwoElementsClosestToZero(A)
A = [10, 8, 3, 5, -9, -7, 6]
TwoElementsClosestToZero(A)
