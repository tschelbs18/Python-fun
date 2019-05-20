def riverSizes(matrix):
    # Write your code here.
	def get_adj_rivers(matrix,row,col):
		adj_rivers = []
		river_len = 1
		matrix[row][col] = 0
		if row < len(matrix) - 1 and matrix[row + 1][col] == 1:
			river_len += get_adj_rivers(matrix,row+1,col)[1]
		if row > 0 and matrix[row - 1][col] == 1:
			river_len += get_adj_rivers(matrix,row-1,col)[1]
		if col > 0 and matrix[row][col-1] == 1:
			river_len += get_adj_rivers(matrix,row,col-1)[1]
		if col < len(matrix[0]) - 1 and matrix[row][col+1] == 1:
			river_len += get_adj_rivers(matrix,row,col+1)[1]
		return [matrix,river_len]
	
		
	final_output = []
	for r_idx, r in enumerate(matrix):
		for c_idx, val in enumerate(r):
			new_river_len = 0
			if val == 0:
				pass
			else: 
				func_results = get_adj_rivers(matrix, r_idx, c_idx)
				matrix = func_results[0]
				river_len = func_results[1]
				final_output.append(river_len)
	return final_output