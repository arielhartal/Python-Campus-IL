def my_mp3_playlist(file_path):
	songs_input = open (file_path, 'r')
	songs_text = songs_input.readlines()
	list_times = []
	list_lines = []
	list_artists = []
	song_counter = 0
	
	for line in songs_text:
		song_counter += 1
		line_for_list = line.replace(";"," ")
		line_for_list = line_for_list.replace("\n","")
		list_lines.append(line_for_list)
		time = line.split(";")
		time = time [2]
		artist = line.split(";")
		artist = artist [1]
		list_artists.append(artist)
		list_times.append(time)
	list_times.sort()
	longest_song_time = list_times[-1]
	
	for song in songs_text:
		if longest_song_time in song :
			longest_song_name = song[:song.find(";")]
	
	most_counter = 0
	most_name = list_artists[0]
	for i in list_artists:
		curr_frequency = list_artists.count(i)
		if curr_frequency > most_counter :
			most_counter = curr_frequency
			most_name = i
	final_tuple = (longest_song_name, song_counter, most_name) 	
	return final_tuple

print(my_mp3_playlist("c:\\Anime\\songs.txt"))	
	 
		