def my_mp4_playlist(file_path, new_song):
	songs_input = open (file_path, 'r')
	songs_text_lines = songs_input.readlines() 
	if len(songs_text_lines) < 3:
		while len(songs_text_lines) < 2 :
			songs_text_lines.append('\n')
		songs_text_lines.append('\n' + new_song)
	else:	
		the_song = songs_text_lines[2]
		the_song = the_song.replace(the_song[:the_song.find(";")],new_song)
		songs_text_lines[2] = the_song
	songs_input = open(file_path, 'w')
	songs_input.writelines(songs_text_lines)
	for line in songs_text_lines :
		print(line)
	songs_input.close()
	
my_mp4_playlist("c:\\Anime\\songs.txt", "Python Love Story")	
