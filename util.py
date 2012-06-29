from urllib.request import urlopen
import json
import sys

def response_to_json(url, enc='utf-8'):
    """Connects to the URL in url and returns the response parsed as json.

    This is useful for retrieving data from RESTful services."""

    response = urlopen(url)

    raw_data = response.read()
    # TODO Determine proper encoding from HTTP headers
    text_data = raw_data.decode(enc)
    json_output = json.loads(text_data)
    return json_output
    
def better_print(message):
    """ Little workaround for using unicode characters on Windows. """
    message_n = message + '\n'
    sys.stdout.buffer.write(message_n.encode(sys.stdout.encoding, 'replace'))