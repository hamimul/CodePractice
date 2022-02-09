#write a fuction that return the first integer appears more than once in an array

def firstDuplicateValue(array):

	found = set()
	for value in array:
		if value in found:
			return value
		found.add(value)
    return -1
