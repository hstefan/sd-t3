from urllib.request import urlopen
import json
import sys
import re

def better_print(message):
    """ Little workaround for using unicode characters on Windows. """
    message_n = message + '\n'
    sys.stdout.buffer.write(message_n.encode(sys.stdout.encoding, 'replace'))

def tweet_has_location(tweet):
    geo_enabled = tweet['user']['geo_enabled']
    coordinates = tweet['coordinates']
    return geo_enabled and coordinates

def get_directions_list(directions_json):
    if len(directions_json['routes']) < 1:
        return None

    dir_info = {}
    route = directions_json['routes'][0]
    steps = route['legs'][0]['steps']
    l = []
    for step in steps:
        l.append(re.sub('<[^<]+?>', '', step['html_instructions']))
    return l
