path = input("Enter a file path:")
task = input("Enter a task:")
with open(path, 'r') as file:
	data = file.read().replace('\n', ' ')
list_data = data.split(" ")
if task == "sort" :
	print(sorted(set(list_data)))
if task == "rev":
	for line in open(path, 'r') :
		print(line[::-1])
if task == "last" :
	n = int(input("Enter a number: "))
	all_lines = open(path, 'r').readlines()
	print(all_lines[n:])
	