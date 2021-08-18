import requests

app_id = '9b5c6e2b'
app_key = '645225db849e26b7c847f95113b4774c'
language = 'en-gb'

def getDefinitions(word_id):
	url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/"+language+"/"+word_id.lower()
	r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
	res = r.json()

	if 'error' in res.keys():
		return False


	output = {}
	senses = res['results'][0]['lexicalEntries'][0]['entries'][0]['senses']
	definitions = []
	for sense in senses:
		definitions.append(f"👉 {sense['definitions'][0]}")
	output['definitions'] = "\n".join(definitions)



	if res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0].get('audioFile'):
		output['audio'] = res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile']


	return output







