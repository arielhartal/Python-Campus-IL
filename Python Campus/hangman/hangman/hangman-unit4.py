letter = input ("Guess a letter: ")

if len(letter)>1 and letter.isalpha() == False:
	print("E3")
	
elif len(letter)>1 :
	print("E1")
	
elif letter.isalpha() == False:
	print("E2")

	
else :	
	print(letter.lower())
	