# isGFG: , Link: 
# IsDone: 0
# A utility function that returns 1 if there is a subset of A[] with sum equal to given sum
def subsetSum (A, n, sum):
	if (sum == 0): 
		return 1
	if (n == 0 and sum != 0):
		return 0
	# If last element is greater than sum, then ignore it
	if (A[n - 1] > sum):
		return subsetSum (A, n - 1, sum)

	return subsetSum (A, n - 1, sum) or subsetSum (A, n - 1, sum - A[n - 1])

 
# Returns 1 if A[] can be partitioned in two subsets of equal sum, otherwise 0
def findPartition(A):
	# calculate sum of all elements
	sum = 0
	n = len(A)
	for i in range(0, n):
		sum += A[i]

	# If sum is odd, there cannot be two subsets with equal sum
	if (sum % 2 != 0):
		return 0

	# Find if there is subset with sum equal to half of total sum
	return subsetSum (A, n, sum / 2)


