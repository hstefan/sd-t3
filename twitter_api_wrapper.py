import json
from urllib.parse import urlencode
from util import response_to_json

def get_twitter_id(username):
    twitter_api_url = "https://api.twitter.com/1/users/show.json?"
    json_output = response_to_json(twitter_api_url + urlencode({'screen_name': username}))
    return json_output['id'] if json_output else None

def get_tweets(user_id, n=10):
    arg_str = urlencode({'id' : str(user_id), 'count' : str(n)})

    api_timeline_url = 'https://api.twitter.com/1/statuses/user_timeline.json?' + arg_str
    json_output = response_to_json(api_timeline_url)

    return json_output
