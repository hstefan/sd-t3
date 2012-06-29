import requests

class TwitterError(Exception):
    def __init__(self, msg):
        if isinstance(msg, requests.models.Response):
            msg = msg.json['error']
        super().__init__(msg)

def get_twitter_id(username):
    """Returns the twitter user id for the username. If no user was found
    raises TwitterError."""

    req = requests.get("https://api.twitter.com/1/users/show.json",
            params={'screen_name': username})

    if req.status_code == 200:
        return req.json['id']
    elif req.status_code == 404:
        raise TwitterError("User not found: '{0}'".format(username))
    else:
        raise TwitterError(req)

def get_tweets(user_id, n=10):
    """Returns a list of at most n tweets for user id user_id."""

    req = requests.get("https://api.twitter.com/1/statuses/user_timeline.json",
            params={'id' : str(user_id), 'count' : str(n)})

    if req.status_code == 200:
        return req.json
    else:
        raise TwitterError(req)
