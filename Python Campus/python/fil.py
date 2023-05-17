def filter_teens(a=13,b=13,c=13):
	if (a>=13 and a<=19) and (a!=15 and a!=16):
		a=fix_age(a)
	elif (b>=13 and b<=19) and (b!=15 and b!=16):
		b=fix_age(b)
	elif (c>=13 and c<=19) and (c!=15 and c!=16):
		c=fix_age(c)
	
	return a+b+c 
	
def fix_age (age): 
	age=0
	return age

print(filter_teens(14,6,10))	