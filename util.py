from urllib.request import urlopen
import json

def response_to_json(url, enc='utf-8'):
	response = urlopen(url)
	raw_data = response.read()
	text_data = raw_data.decode(enc)
	json_output = json.loads(text_data)
	return json_output
