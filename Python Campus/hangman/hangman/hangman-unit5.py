def is_valid_input(letter_guessed):

	if len(letter_guessed)>1 or letter_guessed.isalpha() == False :
		return False
		
	elif len(letter_guessed)==1 and letter_guessed.isalpha() == True:
		return True
		
print(is_valid_input("app&"))		
