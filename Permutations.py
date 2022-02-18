#Write a function that takes in an array of unique integers and return array of all permutation of those integers in no particular orde
#O(n*n!) time | O(n*n!) space
def getPermutations(array):
    # Write your code here.
    permutations = []
	getPermutationsHelper(0,array, permutations)
	return permutations

def getPermutationsHelper(i, array, permutations):
	if i == len(array) - 1:
		permutations.append(array[:])
	else:
		for j in range (i, len(array)):
			swap(array, i, j)
			getPermutationsHelper(i + 1,  array, permutations)
			swap(array, i, j)
			
def swap(array,i,j):
	array[i], array[j] = array[j], array[i]
	