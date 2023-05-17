HANGMAN_PHOTOS = { "First Position" : "x-------x" ,
 "Second Position" : "x-------x \n|\n|\n|\n|\n|\n",
"Third Position" :  "x-------x \n|       |\n|       0\n|\n|\n|\n",
"Fourth Position" :  "x-------x \n|       |\n|       0\n|       |\n|\n|\n",
"Fith Position" :  "x-------x \n|       |\n|       0\n|      /|\\\n|\n|\n",
"Sixth Position" :  "x-------x \n|       |\n|       0\n|      /|\\\n|      /\n|\n",
"Seventh Position" :  "x-------x \n|       |\n|       0\n|      /|\\\n|      / \\\n|\n" }

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

 
print_hangman(3)
