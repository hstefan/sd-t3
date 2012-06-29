from urllib.request import urlopen
import json

def response_to_json(url, enc='utf-8'):
	response = urlopen(url)
	raw_data = response.read()
	text_data = raw_data.decode(enc)
	json_output = json.loads(text_data)
	return json_output
	
def build_arg_string(args, sep='&'):
	arg_str = ''
	for k, v in args.items():
		arg_str = arg_str + k + '=' + 'v' + sep
	return arg_str