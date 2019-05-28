def largestRange(array):
    # Write your code here.
	# Sort it, then determine longest continuation?
	# To improve this, could use a dictionary and iterate through keys
	array.sort()
	max_range_len = 0
	max_range_start = 0
	curr_range_len = 0
	curr_range_start = 0
	curr_range_bool = False
	
	array_set = set(array)
	array_list = list(array_set)
	array_list.sort()
	
	if len(array_list) == 1:
		return [array_list[0],array_list[0]]
	
	for idx, value in enumerate(array_list):
		if idx == 0: 
			pass
		elif value == array_list[idx - 1] + 1:
			if curr_range_bool == False:
				curr_range_bool = True
				curr_range_start = array_list[idx - 1]
				curr_range_len = 1
			else:
				curr_range_len += 1
		elif curr_range_bool:
			curr_range_bool = False
			if curr_range_len > max_range_len:
				max_range_len = curr_range_len
				max_range_start = curr_range_start
				curr_range_len = 0
				curr_range_start = 0
	if curr_range_len > max_range_len:
		max_range_len = curr_range_len
		max_range_start = curr_range_start
	return [max_range_start, max_range_start + max_range_len]
		
		
		
	
