def show_hidden_word(secret_word, old_letters_guessed):
	temp_str = ""
	for i in range(len(secret_word)):
		if secret_word[i] in old_letters_guessed :
			temp_str = temp_str + secret_word[i]
		else:
			temp_str = temp_str + " _ "
			
	return temp_str	


def check_win(secret_word, old_letters_guessed):
	temp_str = ""
	counter = 0
	for i in range(len(secret_word)):
		if secret_word[i] in old_letters_guessed :
			counter += 1
	if counter == len(secret_word) :
		return True
	else :
		return False

		
print(check_win("dee", ['d', 'g', 'e', 'i', 's', 'k', 'y']))
	