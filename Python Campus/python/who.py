def who_is_missing(file_name):
	num_input_file = open(file_name, 'r')
	num_text = num_input_file.read()
	list_num = []
	num_text = num_text.split(",")
	for i in range(len(num_text)):
		list_num.append(int(num_text[i]))
	list_num.sort()	
	missing = ""
	for x in range(list_num[0],len(list_num)):
		if x not in list_num:
			missing = str(x)
	missing_input_file = open("c:\\Anime\\found.txt", 'w')
	missing_input_file.write(missing)
	missing_input_file.close()
	missing_input_file = open("c:\\Anime\\found.txt", 'r')
	missing_text = missing_input_file.read()
	missing_input_file.close()
	num_input_file.close()
			
	return missing_text
	
print(who_is_missing("c:\\Anime\\work.txt"))	