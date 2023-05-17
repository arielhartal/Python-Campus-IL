def copy_file_content(source, destination):
	source_input = open(source, 'r')
	source_text = source_input.read()
	source_input.close()
	destination_input = open (destination, 'w')
	destination_input.write(source_text)
	destination_input.close()
	
	
	
	
	
copy_file_content("c:\\Anime\\work.txt", "c:\\Anime\\vacation.txt")

destination_output = open ("c:\\Anime\\vacation.txt", 'r')
print(destination_output.read())
destination_output.close()
	