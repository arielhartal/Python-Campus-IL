def are_files_equal(file1, file2):
	input_file1 = open(file1, "r")
	input_file2 = open(file2, "r")
	if input_file1.read() == input_file2.read() :
		return True
	else:
		return False
		
file1 = "c:\\Anime\\work.txt"
file2 = "c:\\Anime\\vacation.txt"
print(are_files_equal(file1,file2))