def parse_ranges(ranges_string):
    last_list = []
    ranges_list = ranges_string.split(",")
    gen2 = (i for i in ranges_list)
    for i in gen2:
        help_gen(last_list,i)
    print(last_list)

def help_gen(last_list,ranges_string):
    sub_ranges_list = ranges_string.split("-")
    x=int(sub_ranges_list[0])
    y=int(sub_ranges_list[1])
    generator = (num for num in range(x,y+1))
    for num in generator:
       last_list.append(num)


parse_ranges("0-0,4-8,20-21,43-45")



def get_fibo():
    a, b = 0, 1
    while True:
        yield a
        b = a + b
        yield b
        a = a + b

fibo_gen = get_fibo()
print(next(fibo_gen))
print(next(fibo_gen))












