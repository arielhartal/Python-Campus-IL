def inverse_dict(my_dict):
	rev_dict = {}
	for k, v in my_dict.items():
		rev_dict[v] = rev_dict.get(v, [])
		rev_dict[v].append(k)
	return rev_dict

print(inverse_dict({'I': 3, 'love': 3, 'self.py!': 2}))	