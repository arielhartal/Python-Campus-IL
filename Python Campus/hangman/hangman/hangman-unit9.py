def choose_word(file_path, index):
	words_file = open (file_path, 'r')
	words_file_text = words_file.read()
	list_of_words = words_file_text.split(" ")
	if index > len(list_of_words) :
		index = index - len(list_of_words)
		secret_word = list_of_words[index-1]
	else :
		secret_word = list_of_words[index-1]
	num_of_unique_words = len(list(set(list_of_words)))
	final_tuple = (num_of_unique_words, secret_word)
	return final_tuple


print(choose_word("c:\\hangman\\hangman\\words.txt",15))