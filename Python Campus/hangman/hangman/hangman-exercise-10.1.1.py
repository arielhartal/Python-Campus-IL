import os.path
import os
	


HANGMAN_ASCII_ART = """
 _    _                                         
| |  | |                                        
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| |  | | (_| | | | | (_| | | | | | | (_| | | | |
|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
		     __/ |                      
		    |___/
"""
HANGMAN_PHOTOS = { "First Position" : "x-------x" ,
"Second Position" : "x-------x \n|\n|\n|\n|\n|\n",
"Third Position" :  "x-------x \n|       |\n|       0\n|\n|\n|\n",
"Fourth Position" :  "x-------x \n|       |\n|       0\n|       |\n|\n|\n",
"Fith Position" :  "x-------x \n|       |\n|       0\n|      /|\\\n|\n|\n",
"Sixth Position" :  "x-------x \n|       |\n|       0\n|      /|\\\n|      /\n|\n",
"Seventh Position" :  "x-------x \n|       |\n|       0\n|      /|\\\n|      / \\\n|\n" }
MAX_TRIES = 6



def check_win(secret_word, old_letters_guessed):
	""" checks if the player won or not
	:param secret_word : string of the secret word 
	:param old_letters_guessed: list of letters that the player guessed
	:type secret_word: string
	:type old_letters_guessed: list
	:return: True if all the letters of the secret word are in the
	list of the letters that were guessed and false if not 
	:rtype: boolean
	"""
	letter_counter = 0
	for i in range(len(secret_word)):
		if secret_word[i] in old_letters_guessed :
			letter_counter += 1
	if letter_counter == len(secret_word):
		return True
	else:
		return False
		
		
def show_hidden_word(secret_word, old_letters_guessed):
	"""	Returns a string that contains the letters that are in the correct places of the secret word
	and underscores in the places that are left (the letters the player didnt guess yet)
    :param secret_word: string of the secret word 
    :param old_letters_guessed: list of letters that the player guessed
    :type secret_word: string
    :type old_letters_guessed: list
    :return: A string that contains the letters that are in the secret word and underscores
	in the places of the letters that the player didnt guess yet
    :rtype: String
    """
	new_secret_word = ""
	for i in range(len(secret_word)):
		if secret_word[i] in old_letters_guessed:
			new_secret_word = new_secret_word + secret_word[i]
		else:
			new_secret_word = new_secret_word + "_ "
			
	return new_secret_word
	


def check_valid_input(letter_guessed, old_letters_guessed):
	""" Checks if the input is valid, returns true if it does and false if doesn't
	(valid input = English word that haven't been guessed before)
	:param letter_guessed: string of the letter that the player guessed
    :param old_letters_guessed: list of letters that the player guessed
    :type letter_guessed: string
    :type old_letters_guessed: list
    :return: A true or false statement, true if the input is valid and false if not
    :rtype: Boolean
    """
	if len(letter_guessed)>1 or letter_guessed.isalpha() == False or letter_guessed.lower() in old_letters_guessed:
		return False
	else:
		return True	



def try_update_letter_guessed(letter_guessed, old_letters_guessed):
	""" Uses the check_valid_input function to check if the input is valid or not.
	if the input is valid and has not been guessed before its added to the old_letters_guessed list
	and returns true, if its not valid it prints "X", prints the old_letters_guessed in a string format and returns false
	:param letter_guessed: string of the letter that the player guessed
    :param old_letters_guessed: list of letters that the player guessed
    :type letter_guessed: string
    :type old_letters_guessed: list
	:return: A true statement if the input is valid and hasn't been guessed before,
	false if the input is invalid or been guessed before
	:rtype: boolean
	"""
	if check_valid_input(letter_guessed, old_letters_guessed):
		old_letters_guessed.append(letter_guessed.lower())
		old_letters_guessed.sort
		return True
		
	else:
		print("X")
		old_letters_guessed.sort
		seperator = " -> "
		guessed_letters = seperator.join(old_letters_guessed)
		guessed_letters = guessed_letters[0::].lower() 
		print(guessed_letters)
		return False	
		
				




def choose_word(file_path, index):
	""" Chooses the secret word for the game from the file that contains words
	:param file_path : string of the path to the file 
	:param index: the number of the place of the chosen word 
	:type file_path: string
	:type index: integer
	:return: The secret word that has been chosen for the game
	:rtype: string
	"""
	words_file = open (file_path, 'r')
	words_file_text = words_file.read()
	list_of_words = words_file_text.split(" ")
	words_file.close()
	index = (index - 1) % len(list_of_words)
	secret_word = list_of_words[index]	
	return secret_word
	
	
def print_welcome_screen(welcome_screen, maximum_tries):
	""" Prints the welcome screen and the maximum times the player can guess a letter before losing
	:param welcome_screen : string of the welcome screen 
	:param maximum_tries: the value of the maximum times the player can guess a letter before losing
	:type welcome_screen: string
	:type maximum_tries: integer
	"""
	print(welcome_screen)
	print(maximum_tries)

def print_hangman(num_of_tries):
	""" Prints the positions of the hangman that reflect
	the number of times the player guessed a letter 
	:param num_of_tries : the number of times the player guessed a letter
	:type num_of_tries: integer
	"""
	if num_of_tries == 0:
		print ("Let's start!")
		print(HANGMAN_PHOTOS["First Position"])
	if num_of_tries == 1:
		print(HANGMAN_PHOTOS["Second Position"])
	if num_of_tries == 2:
		print(HANGMAN_PHOTOS["Third Position"])
	if num_of_tries == 3:
		print(HANGMAN_PHOTOS["Fourth Position"])
	if num_of_tries == 4:
		print(HANGMAN_PHOTOS["Fith Position"])
	if num_of_tries == 5:
		print(HANGMAN_PHOTOS["Sixth Position"])
	if num_of_tries == 6:
		print(HANGMAN_PHOTOS["Seventh Position"])	




def main():

	num_of_tries = 0
	old_letters_guessed = []
	
	#Welcome Screen:
	print_welcome_screen(HANGMAN_ASCII_ART, MAX_TRIES)
	file_path = input("Enter file path:")
	# If the file path is wrong, it asks the user for it untill its right
	while os.path.isfile(file_path) == False:
		os.system('cls')
		file_path = input("Enter file path:")
	os.system('cls')	
	index = int(input("Enter index:"))
	os.system('cls')
	secret_word = choose_word(file_path, index)
	#Start Game Screen:
	print_hangman(num_of_tries)
	print(show_hidden_word(secret_word, old_letters_guessed))
	
	#Game Screen:
	while num_of_tries != MAX_TRIES and check_win(secret_word, old_letters_guessed) != True:
		letter = input("Guess a letter:")
		letter = letter.lower()
		os.system('cls')
		if try_update_letter_guessed(letter, old_letters_guessed) == False:
			if letter.isalpha() and len(letter) == 1 and letter not in old_letters_guessed:
				""" If the letter is legal but is wrong and it isn't
				in the old_letters_guessed string it counts as a mistake
				if the letter is legal but is wrong and is in the old_letters_guessed
				string already it doesn't count as a mistake
				"""
				num_of_tries += 1
				
		else:
			if letter not in secret_word:
			# Letter is legal but isn't in the secret word, it counts as a mistake
				num_of_tries += 1
				print(":(\n")
				print_hangman(num_of_tries)
				print(show_hidden_word(secret_word, old_letters_guessed))
			else:
			# This is the case of right answer, then it prints a string with the right letters in the right places
				print(show_hidden_word(secret_word, old_letters_guessed) + "\n")
			
	if check_win(secret_word, old_letters_guessed):
		os.system('cls')
		print("WIN!\n" + "The secret word was: " + secret_word)
		wrong_answers = str(num_of_tries)
		print("Number of wrong answers: " + wrong_answers)
	else:
		os.system('cls')
		print("LOSE!\n" + "The secret word was: " + secret_word)
		wrong_answers = str(num_of_tries)
		print("Number of wrong answers: " + wrong_answers)
		
	#A restart option for the game, if the user want to play again it calls the main function if not it exits	
	responses = {'Y': True, 'N' : False}
	response = input("Do you want to play again? 'Y' for Yes or 'N' for No\n")
	while response not in responses:
		response = input("Do you want to play again? 'Y' for Yes or 'N' for No\n")	
	if response == 'Y':
		os.system('cls')
		main()
	if response == 'N':
		print("Thanks For Playing :)")
		exit()
	
		


if __name__ == "__main__":
    main()

