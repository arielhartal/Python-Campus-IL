import itertools

numbers = iter(list(range(1, 10)))
for i in numbers:
    next(numbers)
    next(numbers)
    print(i)

wallet = [1,1,1,1,1,5,5,10,10,10,10,10,20,20,20]
result = [seq for i in range(len(wallet), 0, -1) for seq in itertools.combinations(wallet, i) if sum(seq) == 100]
result = list(dict.fromkeys(result))
print(len(result))

