"""
sliding-window — variable size with a shrink condition

Trigger: longest or shortest contiguous subarray/substring satisfying a constraint. The word "contiguous" or "substring" is the tell — if order can change, it isn't this. Complexity: O(n) / O(k)
"""

def sliding_window(arr):

def foo():
	return True


l, r = 0, 0
result = None

while r < len(arr):

	# We ususally want to check a condtion or build up some sort of
	# data structure as we go along
	
	# Then we want to check our condition for the problem

	if foo():
	
	#Update some sort of result variable
		pass

	else:
	
		while not foo():
		
			#Condition to increase our left pointer
			#Also remove from any data structure here and update result

			l+=1
			result = r + l
	
	r+=1
	#Consistently increment right pointer in sliding window


return result
