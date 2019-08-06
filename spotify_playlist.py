playlist = {
	'title': 'pop songs',
	'author': 'beatrize',
	'songs': [
		{
		'title': 'song',
		'artist': [
			'artist_name',
			 ],
		'duration': 2.5
		},
		{
		'title': 'song2',
		'artist': [
			'artist_name',
			 ],
		'duration': 2.5
		},
		{
		'title': 'song3',
		'artist': [
			'artist_name',
			 ],
		'duration': 2.5
		}
	] 
}

total_legnth = 0
for song in playlist['songs']:
	total_legnth += song['duration']
print(total_legnth)