import json
from urllib.parse import urlencode
from util import response_to_json

class TwitterError(Exception):
    pass

def get_twitter_id(username):
    """Returns the twitter user id for the username. If no user was found
    raises TwitterError."""

    twitter_api_url = "https://api.twitter.com/1/users/show.json?"
    json_output = response_to_json(twitter_api_url + urlencode({'screen_name': username}))

    if json_output is None:
        raise TwitterError("User not found: '{0}'".format(username))
    else:
        return json_output['id']

def get_tweets(user_id, n=10):
    """Returns a list of at most n tweets for user id user_id."""

    arg_str = urlencode({'id' : str(user_id), 'count' : str(n)})

    api_timeline_url = 'https://api.twitter.com/1/statuses/user_timeline.json?' + arg_str
    json_output = response_to_json(api_timeline_url)

    return json_output
