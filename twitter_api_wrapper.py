import json
from util import response_to_json, build_arg_string

def get_twitter_id(username):
	twitter_api_url = 'https://api.twitter.com/1/users/show.json?screen_name=' + username
	json_output = response_to_json(twitter_api_url)
	return json_output['id'] if json_output else None
	
def get_tweets(user_id, n=10):
	args = {'id' : str(user_id), 'count' : str(n)}
	arg_str = build_arg_string(args)
	
	api_timeline_url = 'https://api.twitter.com/1/statuses/user_timeline.json?' + arg_str
	json_output = response_to_json(api_timeline_url)
	
	return json_output
