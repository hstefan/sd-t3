import json
from urllib.parse import urlencode
from util import response_to_json

def get_twitter_id(username):
    """Returns the twitter user id for the username. If no user was found
    return None."""

    twitter_api_url = "https://api.twitter.com/1/users/show.json?"
    json_output = response_to_json(twitter_api_url + urlencode({'screen_name': username}))
    return json_output['id'] if json_output else None

def get_tweets(user_id, n=10):
    """Returns a list of at most n tweets for user id user_id."""
    assert user_id is not None

    arg_str = urlencode({'id' : str(user_id), 'count' : str(n)})

    api_timeline_url = 'https://api.twitter.com/1/statuses/user_timeline.json?' + arg_str
    json_output = response_to_json(api_timeline_url)

    return json_output
