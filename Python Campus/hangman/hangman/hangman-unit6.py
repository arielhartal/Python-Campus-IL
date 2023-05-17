def check_valid_input(letter_guessed, old_letters_guessed):
	if len(letter_guessed)>1 or letter_guessed.isalpha() == False or letter_guessed in old_letters_guessed or letter_guessed.swapcase() in old_letters_guessed :
		return False
	else:
		return True

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
	if len(letter_guessed)==1 and letter_guessed.isalpha() == True and letter_guessed not in old_letters_guessed and letter_guessed.swapcase() not in old_letters_guessed :
		old_letters_guessed.append(letter_guessed)
		old_letters_guessed.sort
		seperator = " -> "
		final_str = seperator.join(old_letters_guessed)
		final_str = final_str[0::].lower()
		print(final_str)
		return True
		
	else:
		print("X")
		old_letters_guessed.sort
		seperator = " -> "
		final_str = seperator.join(old_letters_guessed)
		final_str = final_str[0::].lower()
		print(final_str)
		return False
	

print(try_update_letter_guessed('b', ['a', 'p', 'c', 'f']))		