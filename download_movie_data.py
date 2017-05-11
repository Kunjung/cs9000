import requests

example = "http://www.omdbapi.com/?t=doctor+strange"

titles = ['Doctor Strange', 'Arrival', 'the autopsy of jane doe']

base = "http://www.omdbapi.com/?t="

for title in titles:
	query = base + title
	r = requests.get(query)
	j = r.json()
	print(j['Plot'])
	print('********************')