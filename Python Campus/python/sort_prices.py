def sort_prices(list_of_tuples):
	list_of_tuples.sort(key = lambda x: x[1])
	return list_of_tuples[-1::-1]






products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
print(sort_prices(products))