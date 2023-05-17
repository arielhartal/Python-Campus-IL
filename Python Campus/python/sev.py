def print_stuff (list_str):
	print(list_str)
	
def print_num (list_str):
	comas = list_str.count(",")
	print(comas+1)

def if_exists (item):
	if item in list_str :
		print ("Yes")
	else :
		print ("No")

def how_much (item):
	return list_str.count(item)		

def del_item (item):
	global list_str
	list_str = list_str.replace(item + ",", "")
	return list_str

def add_item (item):
	global list_str
	list_str = list_str + "," + item
	return list_str	
	
		
def del_illegal(new_list_str):
	num = 0
	for num in range(len(new_list_str)):
		if len(new_list_str[num]) < 3 or new_list_str[num]. isalpha() == False:
			print(new_list_str[num])
			
def del_double (new_list_str):
	temp_list = []
	temp_list = list(set(new_list_str))
	return temp_list
	

list_str = "Me,Meat,Meat,Tomato,Pizza,M%E"
new_list_str = list_str.split(',')	
print(del_double((new_list_str)))

option = input ("Choose option:")
import sys

if option == 1 :
	print_stuff(list_str)
if option == 2 :
	print_num(list_str)
if option == 3 :
	item = input ("Choose item:")
	if_exists(item)
if option == 4 :
	item = input ("Choose item:")
	how_much(item)
if option == 5 :
	item = input ("Choose item:")
	del_item(item)	
if option == 6 :
	item = input ("Choose item:")
	add_item(item)	
if option == 7 :
	del_illegal(new_list_str)
if option == 8 :
	del_double(new_list_str)
if option == 9 :
	sys.exit()