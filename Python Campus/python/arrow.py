def arrow(my_char, max_length):
	num = 0
	for num in range(0,max_length+1) :
		print(my_char * num)
		
	new_num = max_length
	
	for new_num in range(max_length-1,0, -1):
		print(my_char * new_num)
	
arrow('*',5)		