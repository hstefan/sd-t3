from urllib.request import urlopen, HTTPError
import json

def response_to_json(url, enc='utf-8'):
    """Connects to the URL in url and returns the response parsed as json. If
    the request results in a 404 'Not Found' error then None is returned.

    This is useful for retrieving data from RESTful services."""

    try:
        response = urlopen(url)
    except HTTPError as e:
        if e.code == 404:
            return None
        else:
            raise

    raw_data = response.read()
    # TODO Determine proper encoding from HTTP headers
    text_data = raw_data.decode(enc)
    json_output = json.loads(text_data)
    return json_output

def build_arg_string(args, sep='&'):
    arg_str = ''
    for k, v in args.items():
        arg_str = arg_str + k + '=' + v + sep
    return arg_str
