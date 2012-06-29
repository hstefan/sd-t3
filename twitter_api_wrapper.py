import json
from util import response_to_json

def get_twitter_id(username):
	twitter_api_url = 'https://api.twitter.com/1/users/show.json?screen_name=' + username
	json_output = response_to_json(twitter_api_url)
	return json_output['id']