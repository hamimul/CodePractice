def spiralTraverse(array):
    result = [] # save the traversed array
	# startRow = 0 #initial left border 
	# endRow = len(array) - 1 #initial right border
	# startCol = 0 # initial upper border 
	# endCol = len(array[0]) - 1
	# initial botttom border 
	perimeterTraverse(array,0,len(array)-1,0,len(array[0])-1,result)
	return result
	#     >>>>>>>>>>>>>
	#	  ^			  v
	#	  ^			  v
	#	  ^			  v
	#	  ^			  v
	#	  ^			  v
	#     <<<<<<<<<<< v
	#	first we iterate the perimeter of the array
	#	than we will update the border iterativeley 
	#	we can do with recurrsion also if we define
	#	a function with perimeter traverse
	
def perimeterTraverse(array,startRow,endRow,startCol,endCol,result):
	#	traverse complete condition
	if startRow> endRow or startCol > endCol:
		return
	#top border for current perimeter, left to right from border start(including) to end(including) 
	print("top left 2 right")
	for col in range(startCol, endCol+1):
		result.append(array[startRow][col])
		
		print(array[startRow][col])
		
	#right border for current perimeter, top to bottom for start(excluding) to end(including)
	#skip the first one as it has been traversed by top border
	print("right top 2 bottom")
	for row in range(startRow+1, endRow+1):
		result.append(array[row][endCol])
		
		print(array[row][endCol])
	
	#bottom border, in reverse right to left for end(excluding) to start(incuding)
	print("bottom right to left")	
	for col in reversed(range(startCol,endCol)):
		if startRow == endRow:
			break
		result.append(array[endRow][col])
		
		print(array[endRow][col])
	#left border, bottom to top from end(excuding) to start(excluding)
	print("left bottom 2 top")
	for row in reversed(range(startRow+1, endRow)):
		if startCol == endCol:
			break
		result.append(array[row][startCol])
		
		print(array[row][startCol])
	# retraverse the border for new perimeter	
	perimeterTraverse(array,startRow+1,endRow-1,startCol+1,endCol-1,result)	

