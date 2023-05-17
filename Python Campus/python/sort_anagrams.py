def sort_anagrams(list_of_strings):
	anagram_list = []
	for word in list_of_strings :
		if sorted(word) not in anagram_list:
			anagram_list.append(sorted(word))
	in_anagram_list = [[]] * len(anagram_list)
	for word in list_of_strings:
		if sorted(word) in anagram_list :
			index = anagram_list.index(sorted(word))
			in_anagram_list[index] = in_anagram_list[index] + [word]	
	return in_anagram_list			
print(sort_anagrams(['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating', 'ternaries', 'smelters', 'termless', 'salted', 'staled', 'greatening', 'lasted', 'resmelts']))	
				
				