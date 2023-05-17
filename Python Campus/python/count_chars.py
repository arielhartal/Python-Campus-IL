def count_chars(my_str):
	dic = {}
	for i in range(len(my_str)):
		if my_str[i] != " " :
			dic[my_str[i]] = my_str.count(my_str[i])

	return dic
print(count_chars("abra cadabra"))	