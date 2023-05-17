
def sequence_del(my_str):
	new_str = ""
	new_str = my_str[0]
	num = 0
	for num in range(len(my_str)):
		if my_str[num] == new_str[-1] :
			num += 1
		else :
			new_str += my_str[num]
			num += 1
			
	return new_str	

print(sequence_del("SSSSssshhhh"))		