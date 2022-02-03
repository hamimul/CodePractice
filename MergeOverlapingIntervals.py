def mergeOverlappingIntervals(intervals):
    # Write your code here.
	# first we need to sort the intervals with 1st elemnt
    sortedIntervals = sorted (intervals, key=lambda x: x[0])
	
	mergedIntervals = []
	#assign first interval to current
	currentInterval = sortedIntervals[0]
	print(currentInterval)
	#add it to merged
	mergedIntervals.append(currentInterval)
	
	for nextInterval in sortedIntervals:
		#intialize start and end for current interval and next interval
		currentIntervalStart , currentIntervalEnd = currentInterval
		nextIntervalStart , nextIntervalEnd = nextInterval
		print(nextInterval)
		#check overlaping condition
		if currentIntervalEnd >= nextIntervalStart:
			#update current interval in merged intervel
			currentInterval[1] = max(currentIntervalEnd , nextIntervalEnd)
		else:
			#if interval did'nt merged move to next interval keeping it on merged interval
			currentInterval = nextInterval
			mergedIntervals.append(currentInterval)
			
	return mergedIntervals
	
