#Function to return array products for all elemnts except the elemnt
def arrayOfProducts(array):
    # Write your code here.
	finalProducts = [1 for _ in range(len(array)) ]
	leftProducts  = [1 for _ in range(len(array)) ]
	rightProducts = [1 for _ in range(len(array)) ]
	
	leftProduct = 1
	for i in range(len(array)):
		leftProducts[i] = leftProduct
		leftProduct *= array[i]
	
	rightProduct = 1
	for i in reversed(range(len(array))):
		rightProducts[i] = rightProduct
		rightProduct *= array[i]
	
	for i in range(len(array)):
		finalProducts[i] = leftProducts[i] * rightProducts[i]
		
	return finalProducts