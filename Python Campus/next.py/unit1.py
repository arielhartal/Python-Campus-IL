import functools
import math

def double_letter(my_str):
	return "".join([x * 2 for x in my_str])

result = list(map(double_letter, "python"))
print("".join(result))


def four_dividers(number):
	return number % 4 == 0
		
print(list(filter(four_dividers, range(1,3))))

def add(a,b):
	return a+b
	
def sum_of_digits(number):
	return functools.reduce(add, map(int,str(number)))
	
print(sum_of_digits(123))

def combine_coins(coin, numbers):

	return ', '.join(map(lambda s ,n: s + str(n), [coin for i in numbers], numbers))

print(combine_coins('$', range(5)))

def intersection(list_1, list_2):
	return set([x for x in list_1 for x in list_2 if x in list_1 and x in list_2])

print (intersection([5,5,6,7,7], [1,5,9,5,6]))

def is_prime(number):
	return  functools.reduce(lambda x,y: x and y, [number % i != 0 for i in range(2, int(math.sqrt(number)+1))])
print(is_prime(43))

def is_funny(string):
	return not True in map(lambda char: char !='h' and char != 'a' ,string )
print(is_funny("hahahahahaha"))

password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"
print (''.join(map(lambda char: chr(ord(char) + 2), password)))

print (max(open('c:\\files\\names.txt'), key=len))

Lines = open ('c:\\files\\names.txt', 'r').read().replace('\n', '')
print (sum(len(x) for x in Lines))

with open("c:\\files\\names.txt", "r") as input_file: z = min([i for i in input_file.readlines()], key = len)
with open ('c:\\files\\names.txt', 'r') as input_file: print([i for i in input_file.readlines() if len(i) == len(z)])


with open("c:\\files\\names.txt", "r") as test_file: list_of_lengths = [len(i) for i in test_file.read().splitlines()]
print('\n'.join(map(str, list_of_lengths)))
#with open("c:\\files\\names_length.txt", "w") as new_test_file: for i in list_of_lengths: new_test_file.write(str(i) + "\n")
#with open ("c:\\files\\names_length.txt", "r") as new_test_file: print(''.join(i for i in new_test_file.read()))




given_len = int(input("Enter name length:"))
with open ('c:\\files\\names.txt', 'r') as input_file:
	list = list(map(lambda st: str.replace(st, "\n", ""), input_file.readlines()))
	print([i for i in list if len(i) == given_len])



