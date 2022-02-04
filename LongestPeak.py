#function to take an array of integer and return the length of hihest peak
def longestPeak(array):
	longestPeakLength = 0
    i=1
	while i < len(array) - 1:
		isPeak = array[i-1] < array[i] and array[i] > array[i+1]
		if not isPeak:
			i += 1
			continue
			
		leftFoot = i - 2
		while leftFoot >=0 and array[leftFoot] < array[leftFoot + 1]:
			leftFoot -= 1
		
		rightFoot = i + 2
		while rightFoot < len(array) and array[rightFoot-1] > array[rightFoot]:
			rightFoot += 1
			
		currentPeakLength = rightFoot - leftFoot -1
		longestPeakLength =  max(longestPeakLength, currentPeakLength )
		i = rightFoot
	
	return longestPeakLength